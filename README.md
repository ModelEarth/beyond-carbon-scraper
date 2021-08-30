# Carbon Emissions Scraper

Get the most recent [scraped data here](scraped/us-carbon-emissions.json).

For self-hosting you have two options:

## Run in a container

`docker run abriedev/carbon-emissions-scraper scrape`

Save output to a .json file in your root folder

`docker run abriedev/carbon-emissions-scraper scrape > name-of-output-file.json`

## Build from source

__Requires Python 3.8__

1. `make dependencies`
2. `make test`
3. `python3 -m app scrape`
