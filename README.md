# Beyond Carbon Scraper and Fuser

Get the most recent [scraped and fused data here](fused/result.json).

## Build And Run From Source

__Requires Python 3.8__

1. `make dependencies`
2. `make test`
3. `make scrape-and-fuse`

## Run Using Docker

This is a bit tedious:

1. `docker run abriedev/carbon-emissions-scraper scrape_us_carbon_emissions > us_carbon_emissions.json`
2. `docker run abriedev/carbon-emissions-scraper scrape_clean_energy_commitments > clean_energy_commitments.json`
3. `docker run abriedev/carbon-emissions-scraper fuse us_carbon_emissions.json clean_energy_commitments > fused.json`
