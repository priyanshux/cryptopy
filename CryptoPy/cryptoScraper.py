
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'symbol':'BTC'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'Paste Your API KEY',  # Paste your API Key 
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #print(data)
  parseData = json.dumps(response.json())
  #print(parseData)
  ethObj = json.loads(parseData)
  print(ethObj["data"]["BTC"]["name"],end=' ')
  print(ethObj["data"]["BTC"]["quote"]["USD"]["price"],end=" USD\n")

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)