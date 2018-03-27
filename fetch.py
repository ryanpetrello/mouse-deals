#! /usr/bin/env python

# pip install requests BeautifulSoup4
from bs4 import BeautifulSoup
import requests

from datetime import datetime
import subprocess

OUT = 'deals.txt'
URL = 'https://disneyworld.disney.go.com/special-offers/'

def latest():
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.content, 'html.parser')
    with open(OUT, 'w') as f:
        for deal in soup.find_all('article'):
            f.write(deal.find_next('a')['href'])
            f.write('\n')
            details = deal.find_next(attrs={'class': 'details'}).text
            f.write(details.encode('utf-8', 'ignore'))
            f.write(('-' * 80) + '\n')

def push():
    subprocess.call(['git', 'add', OUT])
    subprocess.call(['git', 'commit', '-m', datetime.utcnow().strftime('%Y-%m-%d')])
    subprocess.call(['git', 'push', 'origin', 'master'])

if __name__ == '__main__':
    latest()
    push()
