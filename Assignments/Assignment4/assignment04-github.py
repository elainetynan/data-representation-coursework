import requests
from github import Github
# some_file.py

from config import config as cfg

apikey = cfg["githubkey"]
g = Github(apikey)

#for repo in g.get_user().get_repos():
#    print(repo.name)

# Getting my repository
repo = g.get_repo("elainetynan/data-representation-coursework")
#print(repo.clone_url)

# Getting the url of the AndrewFile.txt file
fileInfo = repo.get_contents("/Assignments/Assignment4/AndrewFile.txt")
urlOfFile = fileInfo.download_url
#print(urlOfFile)

# Getting the text from the AndrewFile.txt file in the repository
response = requests.get(urlOfFile)
contentOfFile = response.text
print(contentOfFile)

# Replacing all instances of 'Andrew' with 'Elaine'
newContents = contentOfFile.replace("Andrew", "Elaine")
print(newContents)

# Writing the content back to the text.txt file in the private repository.
gitHubResponse = repo.update_file(fileInfo.path, "Updated by program", newContents, fileInfo.sha)
print(gitHubResponse)