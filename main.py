import time
from typing import List, Iterable

from returns.result import Result

from models.Car import Car
from scrapers.brcAuto import parse_brc_auto
from scrapers.mollerAuto import parse_moller_auto
from scrapers.inchcape import parse_inchcape

import multiprocessing as mp

if __name__ == "__main__":
    start_time = time.time()
    print("Number of processors: ", mp.cpu_count())
    pool = mp.Pool(mp.cpu_count())

    results: List[Result[Iterable[Car], str]] = []

    [
        pool.apply_async(fn, callback=lambda r: results.append(r))
        for fn in [parse_moller_auto, parse_inchcape, parse_brc_auto]
    ]

    pool.close()
    pool.join()

    print(*results, sep="\n")
    print("--- %s seconds ---" % (time.time() - start_time))
