dependencies:
	pip3 install -r requirements.txt

test:
	python3 -m unittest

scrape-and-fuse:
	mkdir -p scraped
	python3 -m app scrape_us_carbon_emissions > scraped/us-carbon-emissions.json
	python3 -m app scrape_clean_energy_commitments > scraped/clean_energy_commitments.json
	mkdir -p fused
	python3 -m app fuse --out fused/result.json scraped/*.json

container:
	docker build . -t abriedev/carbon-emissions-scraper
