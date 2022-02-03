from getTokenPrice import GetTokenPrice;


def main():
    price = GetTokenPrice("COINGECKO", "BTC")
    price.price_by_coinbase()
    print("BEGIN")


main()
