import requests
from bs4 import BeautifulSoup as bts

def stockPrice(ticker):
    url = f'https://finance.naver.com/item/main.naver?code={ticker}'
    res = requests.get(url)
    soup = bts(markup = res.text, features = 'html.parser')
    items = soup.select('p.no_today > em > span')
    price = items[0].text
    price = int(price.replace(',', ''))
    return f'{ticker}의 현재 가격은 {price:,}원입니다.'
