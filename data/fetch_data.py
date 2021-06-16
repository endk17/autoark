import config
from pathlib import Path
from os import chdir
import datetime
import requests
import cloudscraper

scraper = cloudscraper.create_scraper()


"""
Create Child Directory
"""
path = Path('..')
print(f'Current working directory: {path.cwd()}')

dirName = datetime.datetime.today().strftime('%d-%m-%Y')
path =  Path.cwd() / 'data' / ('{}').format(dirName)
path.mkdir(parents=True, exist_ok=True)


"""
Download CSVs
"""
chdir(path)
print(f'Current working directory: {path.cwd()}')


urls = [
    config.URL_ARKK,
    config.URL_ARKQ,
    config.URL_ARKW,
    config.URL_ARKG,
    config.URL_ARKF,
    config.URL_ARKX,
    config.URL_PRNT,
    config.URL_IZRL 
]

for url in urls:
    print(f"Downloading latest version of {url.split('/')[6]}")

    cfurl = scraper.get(url).content
    name = url.split('/')[6]

    with open(name, 'wb') as f:
        f.write(cfurl)