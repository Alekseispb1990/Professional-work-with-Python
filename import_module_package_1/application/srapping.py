from pprint import pprint

import requests
from bs4 import BeautifulSoup


def pars_url(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    pprint(soup)
