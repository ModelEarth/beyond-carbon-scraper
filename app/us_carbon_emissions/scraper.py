from bs4 import BeautifulSoup
from app.utils.fetcher import Fetcher
import re
import json

URL = "https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_carbon_dioxide_emissions"

def clean_text(input):
    """ Removes repeated spaces, newlines, tabs, nbsp entities, and non-alphanumerics characters
    and converts the string to a number if appropriate."""
    clean_string = re.sub(r'[^a-zA-Z0-9\. ]',"", " ".join(input.split()).replace(u'\xa0',''))
    if clean_string.isdecimal():
        return int(clean_string)
    try:
        return float(clean_string)
    except:
        return clean_string

# https://stackoverflow.com/a/312464
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def scrape(fetcher):
    text, status_code = fetcher.fetch(URL)
    if status_code != 200:
        return {'href': URL, 'error': status_code}

    soup = BeautifulSoup(text, 'html.parser')

    titles =["CO2_rank", "jurisdiction", "CO2_emissions", "CO2_percent", "population", "population_percent", "CO2_per_capita", "CO2_per_1000_miles" ]
    cells = soup.select("#mw-content-text > div.mw-parser-output > table > tbody > tr > td")
    texts = [clean_text(td.get_text()) for td in cells]
    rows = list(chunks(texts, len(titles)))

    build_value = lambda row : {titles[index]:row[index] for index in range(len(titles))}
    result = { row[1]:build_value(row) for row in rows}

    return result

def run(args):
    fetcher = Fetcher(use_cache=args.use_cache, store_cache=args.store_cache)
    scraped = scrape(fetcher)
    fetcher.storeCache()

    if args.out is None:
        print(json.dumps(scraped, indent=2))
    else:
        json.dump(scraped, args.out, ensure_ascii=False)
