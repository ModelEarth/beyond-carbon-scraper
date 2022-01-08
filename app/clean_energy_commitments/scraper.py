import csv
import io
from app.utils.fetcher import Fetcher

# import re
import json

# import functools
import app.clean_energy_commitments.parser_functions as pf

URL = "https://model.earth/apps/beyondcarbon/5_22-data-06_06.csv"


def row_parser(row):
    """
    Parses row of CSV file, including pulling data details from text into more
    usable forms. Returns dictionary for JSON parsing later.
    """
    titles = [
        "jurisdiction",
        "clean_energy_commitment",
        "clean_energy_target_percent",
        "carbon_pollution_reduction_goal_percent",
        "electric_vehicle_goals",
        "energy_efficiency_rank",
    ]

    row_dict = {titles[index]: row[index] for index in range(len(titles))}
    row_dict["energy_efficiency_rank_num"] = pf.energy_eff_rank_num(
        row_dict["energy_efficiency_rank"]
    )
    row_dict.update(pf.clean_energy_commit(row_dict["clean_energy_commitment"]))
    row_dict.update(pf.clean_energy_target_pct(row_dict["clean_energy_target_percent"]))
    row_dict.update(
        pf.carbon_reduction_goal_pct(
            row_dict["carbon_pollution_reduction_goal_percent"]
        )
    )
    row_dict.update(pf.elec_vehicle_goals(row_dict["electric_vehicle_goals"]))
    row_dict.pop("jurisdiction", None)
    return row_dict


def scrape(fetcher):
    text, status_code = fetcher.fetch(URL)
    if status_code != 200:
        return {"href": URL, "error": status_code}

    f = io.StringIO(text)
    rows = csv.reader(f)
    result = {row[0]: row_parser(row) for row in rows}
    return result


def run(args):
    fetcher = Fetcher(use_cache=args.use_cache, store_cache=args.store_cache)
    scraped = scrape(fetcher)
    fetcher.storeCache()

    if args.out is None:
        print(json.dumps(scraped, indent=2))
    else:
        json.dump(scraped, args.out, ensure_ascii=False)
