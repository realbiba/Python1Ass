from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
result = cg.get_coins_markets(vs_currency='usd')
