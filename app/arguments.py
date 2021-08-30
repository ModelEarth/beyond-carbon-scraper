import argparse


def parse(args):
    parser = argparse.ArgumentParser(
        description="Scrape Wikipedia Carbon Emissions data ")
    subparser = parser.add_subparsers(
        dest="command", required=True)
    parser_scrape = subparser.add_parser(
        'scrape', description="Scrape the US Carbon Footprint page")
    parser_scrape.add_argument(
        '--out', dest="out", default=None, type=argparse.FileType('w', encoding='UTF-8'), help="save output here.")
    group = parser_scrape.add_mutually_exclusive_group()
    group.add_argument(
        '--use-cache', dest='use_cache', type=argparse.FileType('r'), help='read HTML from this file.')
    group.add_argument(
        '--store-cache', dest='store_cache', type=argparse.FileType('w', encoding='UTF-8'), help='store HTML into this file')

    return parser.parse_args(args)
