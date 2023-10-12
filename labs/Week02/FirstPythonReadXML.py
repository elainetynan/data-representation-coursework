import requests
#page = requests.get("company.xml")
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)
print("---------------------")
print(page.content)


#with open(company.xml) as fp:

################
# Not working!!!