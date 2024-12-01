import requests

class ArbitrageAgent:
    def __init__(self):
        pass

    def execute(self):
        print("EXECUTING ARBITRAGE STRATEGY...")
        try:
            response = requests.get('https://api.coinmarketcap.com/data-api/v3/topsearch/rank')
            if response.status_code == 200:
                data = response.json()
                print("ARBITRAGE DATA:", data)
            else:
                print("FAILED TO FETCH MARKET DATA.")
        except Exception as e:
            print(f"ERROR DURING ARBITRAGE EXECUTION: {e}")