import requests

url = "http://atu.ie"

response = requests.get(url)
print(response.headers)
print("~~~"+str(response.status_code)+"~~~")
