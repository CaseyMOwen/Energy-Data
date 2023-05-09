import requests
import config

baseURL =  "https://api.eia.gov/v2/"
route = "electricity/electric-power-operational-data"
keyURL = "?api_key=" + config.APIKey
finalURL = baseURL + route + keyURL

headers = {
    "frequency" : "quarterly",
    "data" : "consumption-for-eg-btu",
    "facets" : "",
    "start" : "2022-Q1",
    "end" : "null",
    "sort": [
        {
            "column": "period",
            "direction": "desc"
        }
    ],
    "offset": 0,
    "length": 5000
    
}

response = requests.request("GET", finalURL, headers = headers)