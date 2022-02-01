from flask import Blueprint, jsonify,render_template,redirect,request, request_finished
import json
import sys
sys.path.append("/")
#define global variable to save data 
data = []
index = Blueprint(__name__, "index")
@index.route("/")
def home():
    return render_template("index.html")

@index.route("/location")
def locate():
    import GetGeoLocationFromAPI
    currentlocation = GetGeoLocationFromAPI.getGeo()
    return jsonify(currentlocation)
@index.route("/submit",methods = ["POST"])
def submit():
    if request.method == "POST":
        
        markers = json.loads(request.get_data(as_text=True))["value"]
        instructions = 
        return "OK"
@index.route("/car")
def car():
    global data
    if len(data) == 0:
        return "OK"
    return jsonify(data)
  


