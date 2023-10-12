import requests
url = "https://someurl.com"
response = requests.get(url)
data = response.json()
print(data)
