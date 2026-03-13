import requests

URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def get_crypto_price():

    response = requests.get(URL)

    data = response.json()

    price = data["bpi"]["USD"]["rate"]

    print("Bitcoin Price (USD):", price)

if __name__ == "__main__":
    get_crypto_price()
