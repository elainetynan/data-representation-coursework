import requests
import json

#url = "currentprice.json"
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)
data = response.json()
#print(data)
#with open("bitcoindump.json") as fp:
#    json.dump(data, fp)

euroPriceObject = data["bpi"]["EUR"]

#print(euroPriceObject)
rate = euroPriceObject["rate"]
print(rate)