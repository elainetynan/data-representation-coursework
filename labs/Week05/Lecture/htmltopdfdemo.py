import requests
import urllib.parse
from config import config as cfg

targetUrl = "https://en.wikipedia.org"
#targetUrl = "https://www.atu.ie/"

apiKey = cfg["htmltopdfkey"]
#api = "yourkey"

apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'url': targetUrl,'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)

requestUrl = apiurl +"?" + parsedparams 
print (requestUrl)

response = requests.get(requestUrl)

print (response.status_code)
result =response.content

with open("document.pdf", "wb") as handler:
    handler.write(result)

# https://api.html2pdf.app/v1/generate?url=https%3A%2F%2Fen.wikipedia.org&apiKey=eAs3mWn7R59gxZ6kSYysYdpTUsivY7Am74aSN36pOHdMMyTu3XDpdSOtaAySz3qF
# 200

# C:\Users\elaine.tynan\OneDrive - TUS MM\HDip\Semester1\ProgrammingScripting\Cmder\vendor\git-for-windows\mingw64\lib\python3.9