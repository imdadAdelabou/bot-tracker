from constant import BINANCE_API_URL, BINANCE_AVG_PRICE_ROUTE, BINANCE_TICKER_PRICE_ROUTE
import requests

class BinanceApi:
    def __init__(self):
       print("BINANCE API")
    
    def get_token_price(self, token = "BTC", conversion_peer = "USDT"):
        url = "{}{}".format(BINANCE_API_URL, BINANCE_TICKER_PRICE_ROUTE)
        params = {
            "symbol": token + conversion_peer
        }
        result = requests.get(url, params=params)
        price = result.json()["price"]
        return float(price)