
import sys
import requests

def main():

    #check the aurguement
    if len(sys.argv)!=2:
        sys.exit("Missing command-line argument")

    try:
        num=float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    #get the price of bitcoin as a float
    try:
        #generated api key
        url="https://rest.coincap.io/v3/assets/bitcoin?apiKey=54d6aa0203c21593848e5b45c06b21fe4461cee782993327ebc2a6a304ac6671"
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()
        price =float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit(1)

    #calculating the price
    total=num*price
    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()
