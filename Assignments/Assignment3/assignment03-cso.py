from ast import Pass
import requests
import json

urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAll(dataset):   
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    # Putting cso.json file in this current directory as I don't want to overwrite
    # the one in the root directory of my repository from class examples.
    with open("./Assignments/Assignment3/cso.json", "wt") as fp:
        print(json.dumps(getAll("FIQ02")), file=fp)