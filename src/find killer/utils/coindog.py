#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import time
import requests, json

host = "47.96.171.142"
user = 'root'
pswd = '123456'
dbname='echain'

symbols = [
    'BTCUSDT',
    'ETHUSDT',
]
exs = [
    'HUOBIPRO',
    'HUOBI-POOL-ECO',
    'GATEIO',
    'BINANCE',
    'OKEX',
    'MXC',
    'BIGONE',
    'ZB',
    'YOUBI',
    'KUCOIN',
    'POLONIEX',
    'BITZ',
    'BIKICOIN',
    'BIBOX',
    'ZG',
    'DIGIFINEX',
    'LBANK',
    'BKEX',
    'COINTIGER',
    'COINBENE',
    'BGOGO',
    'COINSUPER',
    'DOBITRADE',
    '58COIN',
    'TOKOK',
    'ZBG',
    'BW',
    'AEX',
    'BIKICOIN',
    'BBKX',
    'BITSG',
    'RIGHTBTC',
    'GOKO',
    'EBUYCOIN',
    # 'OKCOIN',
    'COINEGG',
    # 'BITMAX',
]

def update(_coin, _currency, _symbol, _high, _low, _open, _close, _exchange_name, _time = time.time()):

    # 打开数据库连接
    db = MySQLdb.connect(host, user, pswd, dbname, charset='utf8mb4')

    # sql = """INSERT INTO `tickers` (`base`, `currency`, `symbol`, `high_price`, `low_price`, `open_price`, `close_price`, `exchange_name`, `update_time`)
    #     VALUES('BTC', 'USDT', 'BTCUSDT', '61512.12713304667350', '58970.63530801362825','59065.33243911680550','57920.51289144851775', 'HuobiPro', 1524630942)"""
    sql = """INSERT INTO `tickers` (`base`, `currency`, `symbol`, `high_price`, `low_price`, `open_price`, `close_price`, `exchange_name`, `update_time`)
        VALUES('{0}', '{1}', '{2}', '{3}', '{4}','{5}','{6}', '{7}', {8}) ON DUPLICATE KEY UPDATE
        base = VALUES(base), currency = VALUES(currency),symbol = VALUES(symbol),high_price = VALUES(high_price),low_price = VALUES(low_price),
        open_price = VALUES(open_price), close_price = VALUES(close_price), exchange_name = VALUES(exchange_name), update_time = VALUES(update_time)""".format(_coin, _currency, _symbol, _high, _low, _open, _close, _exchange_name, _time)

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    print(cursor.execute(sql))
    db.commit()

    # 关闭数据库连接
    db.close()

def coindog(ex,symbol):
    url = "http://api.coindog.com/api/v1/tick/{0}:{1}?unit=usd".format(ex, symbol)
    r = json.loads(requests.get(url).text)
    if 'dateTime' not in r:
        print('request error',ex)
        return

    timestamp = time.time()
    datetime = int(r['dateTime'] / 1000)
    if datetime <  (timestamp - 3600) or r['high'] == 0:
        print('result of the useless.',ex)
        return

    coin = r['base']
    currency = r['currency']
    symbol = r['symbol']
    high = str(r['high'])
    low = str(r['low'])
    open = str(r['open'])
    close = str(r['close'])
    exchange_name = r['exchangeName'] + '[coindog]'

    update(coin, currency, symbol, high, low, open, close, exchange_name, datetime)


for symbol in symbols:
    for ex in exs:
        coindog(ex,symbol)