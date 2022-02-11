from exchanges.binance_api import BinanceApi
from exchanges.kucoin_api import KucoinApi
from getTokenPrice import GetTokenPrice;


def main():
    try:
        # price = GetTokenPrice("COINGECKO", "BTC")
        # price.price_by_coinbase()
        # print("====>>BINANCE<<<======")
        # binance_api = BinanceApi()
        # print(str(binance_api.get_token_price()))
        print("====>> KUCOIN <<=====")
        result = KucoinApi().get_token_price()
        print(result)
    except Exception as e:
        print(e)

main()
