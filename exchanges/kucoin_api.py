import requests

from constant import KUCOIN_API_URL, KUCOIN_GET_TICKET_ROUTE

class KucoinApi:
    def get_token_price(self, token="BTC", conversion_peer="USDT"):
        url = KUCOIN_API_URL + KUCOIN_GET_TICKET_ROUTE
        params = {
            "symbol":  token+"-"+conversion_peer
        }
        response = requests.get(url, params=params)
        content = response.json()
        return float(content["data"]["price"])