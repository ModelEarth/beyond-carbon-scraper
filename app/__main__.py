import sys

import app.us_carbon_emissions.scraper
import app.clean_energy_commitments.scraper
import app.arguments

if __name__ == '__main__':
    args = app.arguments.parse(sys.argv[1:])

    commands = {
        "scrape_us_carbon_emissions": app.us_carbon_emissions.scraper.run,
        "scrape_clean_energy_commitments": app.clean_energy_commitments.scraper.run,
    }

    commands[args.command](args)
