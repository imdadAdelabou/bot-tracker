from exchanges.binance_api import BinanceApi
from getTokenPrice import GetTokenPrice;


def main():
    price = GetTokenPrice("COINGECKO", "BTC")
    price.price_by_coinbase()
    print("====>>BINANCE<<<======")
    binance_api = BinanceApi()
    print(str(binance_api.get_token_price("ETH")))

main()
