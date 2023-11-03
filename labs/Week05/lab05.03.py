import requests
from github import Github
# some_file.py

from config import config as cfg

apikey = cfg["githubkey"]
g = Github(apikey)

#for repo in g.get_user().get_repos():
#    print(repo.name)

# Getting my private repository
repo = g.get_repo("elainetynan/aprivateone")
#print(repo.clone_url)

# Getting the url of the text.txt file
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)

# GEtting the text from the test.txt file in the private repository
response = requests.get(urlOfFile)
contentOfFile = response.text
print(contentOfFile)

# concatenatinng on more stuff
newContents = contentOfFile + " more stuff \n"
print(newContents)

# Writing the content back to the text.txt file in the private repository.
gitHubResponse = repo.update_file(fileInfo.path, "Updated by program", newContents, fileInfo.sha)
print(gitHubResponse)