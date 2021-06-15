#! /usr/bin/env python

# pip install requests BeautifulSoup4
from bs4 import BeautifulSoup
import requests

from datetime import datetime
import subprocess

OUT = 'deals.txt'
URL = 'https://disneyworld.disney.go.com/special-offers/'

def latest():
    resp = requests.get(URL, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0'
    })
    soup = BeautifulSoup(resp.content, 'html.parser')
    with open(OUT, 'w') as f:
        for deal in soup.find_all('article'):
            f.write(deal.find_next('a')['href'])
            f.write('\n')
            details = deal.find_next(attrs={'class': 'details'}).text
            f.write(details)
            f.write(('-' * 80) + '\n')

if __name__ == '__main__':
    latest()
