from constant import AUTHORIZATION_VALUE, COINBASE_ROUTE_PRICE, HEADER_REQ
import requests


class CoinbaseApi:
    def __init__(self, token, pair = "USD"):
        self.token = token
        self.pair = pair

    def get_buy_price(self): #Le prix qu"il faut pour acheter une cryptomonnaie
       return self.get_value("/buy")

    def get_sell_price(self): #le prix de base a laquelle une crypto peut etre vendu
       return self.get_value("/sell")

    def get_spot_price(self): #le prix que vaux une cryptomonnaie
       return self.get_value("/spot")

    def get_value(self, routeName):
        url = "{}{}-{}{}".format(COINBASE_ROUTE_PRICE, self.token, self.pair, routeName)
        result = requests.get(url, headers=HEADER_REQ)
        body_content = result.json()
        amount = body_content['data']['amount']
        return float(amount)