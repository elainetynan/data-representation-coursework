import requests
import json
from config import config as cfg

#filename = "repos-public-contents-code.json"
#filename = "repos-public-contents.json"
#filename = "repos-public.json"
filename = "repos-private.json"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents'
#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation'
url = 'https://api.github.com/repos/elainetynan/aprivateone'

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

#apikey = cfg["githubkey"]
apikey = "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"
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)