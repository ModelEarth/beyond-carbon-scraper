import argparse


def parse(args):
    parser = argparse.ArgumentParser(
        description="Scraper and Fuser for Beyond Carbon Challenge ")
    subparser = parser.add_subparsers(
        dest="command", required=True)
    parser_1 = subparser.add_parser(
        'scrape_us_carbon_emissions', description="Scrape the US Carbon Footprint Wikipedia page")
    parser_1.add_argument(
        '--out', dest="out", default=None, type=argparse.FileType('w', encoding='UTF-8'), help="save output here.")
    group = parser_1.add_mutually_exclusive_group()
    group.add_argument(
        '--use-cache', dest='use_cache', type=argparse.FileType('r'), help='read HTML from this file.')
    group.add_argument(
        '--store-cache', dest='store_cache', type=argparse.FileType('w', encoding='UTF-8'), help='store HTML into this file')

    parser_2 = subparser.add_parser(
        'scrape_clean_energy_commitments', description="Scrape the Clean Energy Commitments CSV")
    parser_2.add_argument(
        '--out', dest="out", default=None, type=argparse.FileType('w', encoding='UTF-8'), help="save output here.")
    group = parser_2.add_mutually_exclusive_group()
    group.add_argument(
        '--use-cache', dest='use_cache', type=argparse.FileType('r'), help='read HTML from this file.')
    group.add_argument(
        '--store-cache', dest='store_cache', type=argparse.FileType('w', encoding='UTF-8'), help='store HTML into this file')

    return parser.parse_args(args)
