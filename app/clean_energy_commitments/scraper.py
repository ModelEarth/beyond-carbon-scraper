import csv
import io
from app.utils.fetcher import Fetcher
import re
import json
import functools

URL = "https://model.earth/apps/beyondcarbon/5_22-data-06_06.csv"

def scrape(fetcher):
    text, status_code = fetcher.fetch(URL)
    if status_code != 200:
        return {'href': URL, 'error': status_code}

    titles = ["juristiction","clean_energy_commitment","clean_energy_target_percent","carbon_pollution_reduction_goal_percent","electric_vehicle_goals","energy_efficency_rank"]

    build_value = lambda row : {titles[index]:row[index] for index in range(len(titles))}

    f = io.StringIO(text)
    rows = csv.reader(f)
    result = { row[0]:build_value(row) for row in rows}
    return result


def run(args):
    fetcher = Fetcher(use_cache=args.use_cache, store_cache=args.store_cache)
    scraped = scrape(fetcher)
    fetcher.storeCache()

    if args.out is None:
        print(json.dumps(scraped, indent=2))
    else:
        json.dump(scraped, args.out, ensure_ascii=False)
