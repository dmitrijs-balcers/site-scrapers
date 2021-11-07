from typing import Iterable, Optional, Dict, Any, Callable

from gazpacho import Soup
from returns.pipeline import flow
from returns.maybe import Maybe, Nothing, Some
from returns.pointfree import bind
from returns.result import Result, Success, Failure

from models.Car import Car, CarDate


def parse_brc_auto() -> Result[Iterable[Car], str]:
    soup = Soup.get("https://lv.brcauto.eu/lietoti-auto?city=5&search=1&driving_wheelbase=3")

    cars = soup.find("div", {"class": "cars"}, partial=False)

    if type(cars) is not list:
        return Failure("failed to acquire cars")

    def parse_car(car: Soup) -> Car:
        car_top = flow(
            car,
            find_one("h2", {"class": "cars__title"}),
            bind(find_one("a"))
        )

        url = flow(
            car_top.map(lambda _: _.attrs),
            lambda attrs: attrs.map(lambda _: _["href"]),
            lambda href: href.value_or("")
        )
        summary = car_top.map(lambda _: _.text).value_or("")
        details = find_one("p", {"class": "cars__subtitle"})(car) \
            .map(lambda _: _.text.split("|")) \
            .value_or(["", "", "", "", ""])
        price = find_one("div", {"class": "cars-price"})(car).map(lambda _: _.text).value_or("")
        return Car(
            url=url.strip(),
            summary=summary.strip(),
            transmission=details[2].strip(),
            hp=details[4].strip(),
            date=CarDate("00", details[0].strip()),
            type="-",
            price=price.strip()
        )

    return Success([parse_car(car) for car in cars])


def find_one(tag: str, attrs: Optional[Dict[str, Any]] = None) -> Callable[[Soup], Maybe[Soup]]:
    def _(soup: Soup) -> Maybe[Soup]:
        result = soup.find(tag, attrs)

        if type(result) is Soup:
            return Some(result)

        if type(result) is list:
            return Some(result[0])

        return Nothing

    return _