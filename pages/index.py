from flask import Blueprint, jsonify,render_template,redirect,request
import json
import sys
sys.path.append("/")
index = Blueprint(__name__, "index")
@index.route("/")
def home():
    return render_template("index.html")

@index.route("/location")
def locate():
    import GetGeoLocationFromAPI
    currentlocation = GetGeoLocationFromAPI.getGeo()
    return jsonify(currentlocation)
# @index.route("/Latitude")
# def Latitude():
#      import geocoder
#      g = geocoder.ip('me')
#      return str(g.latlng[0])
# @index.route("/Longtitude")
# def Longtitude():
#      import geocoder
#      g = geocoder.ip('me')
#      return str(g.latlng[1])
@index.route("/caculate",methods = ["POST"])
def calculate():
    import Caculate
    if request.method == "POST":
        arr = json.loads(request.get_data(as_text=True)["value"])
        print(json.loads(request.get_data(as_text=True)["value"]))
    return "Hehehe"
