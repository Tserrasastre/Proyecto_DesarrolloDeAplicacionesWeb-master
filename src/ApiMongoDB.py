import requests
import json

def ApiMongoDB():
    url = "https://data.mongodb-api.com/app/data-qnzsx/endpoint/data/v1/action/find"

    payload = json.dumps({
        "collection": "AllBikesCollection",
        "database": "BikesRentalDB",
        "dataSource": "BikeCluster",
        "filter":{
            
        }
        
    })
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': "a5AKzDuv7g8qEwFuZWSWzhOuTew36LO1EwdsLG8L3STziDlZ6YksSQfyvkIFAHIJ", 
    'Accept': 'aplication/ejson'
    }

    BikesRentalDB = requests.post(url, headers=headers, data=payload)
    BikesRentalDB = BikesRentalDB.text
    apitoJson = open("DataBase/AllBikes.json","w+",encoding="UTF-8")
    apitoJson.write(BikesRentalDB)

if __name__ == "__main__":
    ApiMongoDB()
