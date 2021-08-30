dependencies:
	pip3 install -r requirements.txt

test:
	python3 -m unittest

scrape:
	python3 -m app scrape > scraped/us-carbon-emissions.json

container:
	docker build . -t abriedev/carbon-emissions-scraper
