from asyncio import constants
from email import header
from sqlite3 import paramstyle
import requests
from constant import COINBASE_ROUTE_PRICE
from exchanges.coinbase_api import CoinbaseApi

class GetTokenPrice:
    def __init__(self, exchange, token):
        self.exchange = exchange
        self.token = token

    def get_token_price(self):
        print(self.exchange)
        print("get Token")

    def price_by_coinbase(self):
        coin_base_api = CoinbaseApi("BTC")
        print("SPOT PRICE ==>>" + str(coin_base_api.get_spot_price()))
        print("Buy price ==>>> " + str(coin_base_api.get_buy_price()))
        print("Sell price ===>> " + str(coin_base_api.get_sell_price()))

    