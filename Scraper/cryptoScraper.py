# API used = CryptoCompare

import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import csv
import asyncio
import datetime


url_for_minute_data = 'https://min-api.cryptocompare.com/data/histominute'
url_for_hour_data = 'https://min-api.cryptocompare.com/data/histohour'

# curreny symbols: 'BTC' for bitcoin, 'ETH' for ethereum, 'LTC' for litecoin and 'XRP' for ripple
Currency = 'BTC'


def write_to_file(symbol, data):
    with open('BTCUSDT_sample_data.csv', mode='a', newline='') as data_file:
        # this generates time in UTC (not IST)
        date = datetime.datetime.fromtimestamp(data["time"]).strftime('%Y-%m-%d %H:%M:%S')
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow([data["time"], date, data["open"], data["high"], data["low"], data["close"], data["volumefrom"], data["volumeto"]])


async def get_minute_data_current(symbol):

    while True:
        parameters = {
            'fsym': symbol,
            'tsym': 'USDT',
            'limit': '1',
            'aggregate': '1'
        }

        try:
            response = requests.get(url_for_minute_data, params=parameters)
            data = response.json()["Data"][0]
            write_to_file(symbol, data)
            print("Executed")

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

        # Every minute (60 seconds)
        await asyncio.sleep(60)


def stop():
    task.cancel()


loop = asyncio.get_event_loop()

# Stops after 5 minutes (300 seconds)
loop.call_later(300, stop)

task = loop.create_task(get_minute_data_current(Currency))
try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass
