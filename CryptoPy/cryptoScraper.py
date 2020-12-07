# API used = Nomics

import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


url = 'https://api.nomics.com/v1/currencies/ticker'

key = 'ENTER YOUR API KEY'
Currency = 'BTC'


# enter your api key from nomics in "key"
# curreny symbols: 'BTC' for bitcoin, 'ETH' for ethereum, 'LTC' for litecoin and 'XRP' for ripple
def getPrice(key, currencySymbol, interval='1hr'):
    parameters = {
        'key': key,
        'ids': currencySymbol,
        'interval': interval,
        'convert': 'USDT'
    }

    try:
        response = requests.get(url, params=parameters)
        data = response.json()
        price = [dp["price"] for dp in data]
        return(', '.join(price))

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


newPrice = getPrice(key, Currency)
print(newPrice)
