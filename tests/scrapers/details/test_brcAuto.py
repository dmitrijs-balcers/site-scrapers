import unittest
import os

from models.Car import CarFull, CarDate
from scrapers.details.brcAuto import scrape_brc_auto_car_detail
from scrapers.details.inchcape import scrape_inchcape_car_detail

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


class UtilsTestCase(unittest.TestCase):
    def test_mercedes_ml_500(self) -> None:
        with open(os.path.join(THIS_FOLDER, "brc_data/brc_mercedes_ml_500.html")) as car:
            self.assertEqual(CarFull(
                url='https://lv.brcauto.eu/automobilis/c834749-mercedes-benz-ml-500-5.5l-automatiska',
                previewImgSrc='https://media.brcauto.eu/cars/all/834749_1.jpg',
                summary='Mercedes-Benz ML 500',
                date=CarDate(month='00', year='2007'),
                type='Apvidus',
                transmission='Automātiskā',
                hp='285 Kw (388 HP)',
                price=9000,
                vin='WDC1641721A343529',
                registrationNo=None,
                mileage=253770,
                engineSize=None,
                techInspDate=None,
                fuelType='petrol',
                body="suv",
                drivetrain='awd',
                color=None,
                hasWarranty=False,
                doors="5",
                country='lv',
                dealer='brc'
            ), scrape_brc_auto_car_detail(car.read()))

    def test_ford_focus(self) -> None:
        with open(os.path.join(THIS_FOLDER, "brc_data/brc_ford_focus.html")) as car:
            self.assertEqual(CarFull(
                url='https://lv.brcauto.eu/automobilis/c832614-ford-focus-1.5l-mehaniska',
                previewImgSrc='https://media.brcauto.eu/cars/all/832614_1.jpg',
                summary='Ford Focus',
                date=CarDate(month='00', year='2016'),
                type='Universālis',
                transmission='Mehāniskā',
                hp='88 Kw (120 HP)',
                price=8500,
                vin='WF06XXGCC6GC82052',
                registrationNo=None,
                mileage=143343,
                engineSize=None,
                techInspDate=None,
                fuelType='diesel',
                body="wagon",
                drivetrain='fwd',
                color=None,
                hasWarranty=False,
                doors="5",
                country='lv',
                dealer='brc'
            ), scrape_brc_auto_car_detail(car.read()))

    def test_bmw_220(self) -> None:
        with open(os.path.join(THIS_FOLDER, "brc_data/brc_bmw_220.html")) as car:
            self.assertEqual(CarFull(
                url='https://lv.brcauto.eu/automobilis/c832466-bmw-220-2.0l-mehaniska',
                previewImgSrc='https://media.brcauto.eu/cars/all/832466_1.jpg',
                summary='BMW 220',
                date=CarDate(month='00', year='2015'),
                type='Kupeja',
                transmission='Mehāniskā',
                hp='140 Kw (190 HP)',
                price=12900,
                vin='WBA2G71090VZ11343',
                registrationNo=None,
                mileage=219814,
                engineSize=None,
                techInspDate=None,
                fuelType='diesel',
                body="coupe",
                drivetrain='rwd',
                color=None,
                hasWarranty=True,
                doors="2",
                country='lv',
                dealer='brc'
            ), scrape_brc_auto_car_detail(car.read()))


if __name__ == '__main__':
    unittest.main()