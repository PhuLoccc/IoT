import json
import requests
def outPutdata(obj):
    print(obj)

def distanceCalculation(arrayObj):
    response = requests.get()


import requests

url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=10.822445410414515,106.68826566827614&destinations=10.822474966239396,106.68832467687447&key=AIzaSyCV7EHyN-qOilgx_e_IIGtwaDy1_cn5YRs"
str = str.format("https://maps.googleapis.com/maps/api/distancematrix/json?origins={},{}&destinations={},{}&key=AIzaSyCV7EHyN-qOilgx_e_IIGtwaDy1_cn5YRs",10.804570267514782,106.69285730902345,10.80446018812232,106.69256226603181)

payload={}
headers = {}

response = requests.request("GET", str, headers=headers, data=payload)
# Latitude: 10.822445410414515 | Longitude: 106.68826566827614
# Latitude: 10.822474966239396 | Longitude: 106.68832467687447

#10.798069581461503 | 106.62215620611718
#10.442276496893571 | 107.16711717487851
print(response.text) 
