import requests
import json
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


url = 'https://api.nomics.com/v1/currencies/ticker'



#enter your api key from nomics in "key"
#curreny symbols: 'BTC' for bitcoin, 'ETH' for ethereum, 'LTC' for litecoin and 'XRP' for ripple
def getPrice(key, currencySymbol, interval = '1hr'):
    parameters = {
        'key': key,
        'ids': currencySymbol,
        'interval': interval,
        'convert': 'USDT'
    }

    try:
        response = requests.get(url, params=parameters)
        # print(response.json())
        data = response.json()
        for dp in data:
            price = dp["price"]
            # print(dp["symbol"] + ': ' + price)
        return price

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

newPrice = getPrice(key = '2a106acc5e2e1abb424ae177ba6bf929', currencySymbol= 'BTC')
print(newPrice)