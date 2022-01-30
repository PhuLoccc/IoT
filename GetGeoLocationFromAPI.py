import requests
import json
def getGeo():
    #API KEY is required
    response = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyB8DKlqACwhsXV3splf60RvQJQrqQJNb4c")
    obj = json.loads(response.text)
    return {"lat":obj["location"]["lat"],"lng":obj["location"]["lng"]}
