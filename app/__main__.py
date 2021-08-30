import sys

import app.us_carbon_emissions.scraper
import app.arguments

if __name__ == '__main__':
    args = app.arguments.parse(sys.argv[1:])

    commands = {
        "scrape": app.us_carbon_emissions.scraper.run,
    }

    commands[args.command](args)
