import requests
from bs4 import BeautifulSoup as bts
import pandas as pd

def stockPriceDaily(ticker, page = 1):
    url = f'https://finance.naver.com/item/sise_day.naver?code={ticker}&page={page}'
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    res = requests.get(url, headers = {'user-agent': ua})
    soup = bts(markup = res.text, features = 'html.parser')
    items = soup.select('table')
    tbls = pd.read_html(str(items))
    return tbls[0].dropna().reset_index(drop = True)