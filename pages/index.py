from flask import Blueprint, jsonify,render_template,redirect,request, url_for
import json
import sys
sys.path.append("/")
#define global variable to save instructions 
instructions = []
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
    global instructions
    if request.method == "POST":
        import RoadRoute
        markers = json.loads(request.get_data(as_text=True))["value"]
        instructions = RoadRoute.get_instructions(markers)
    return "OK"
@index.route("/car")
def car():
    global instructions
    if len(instructions) == 0:
        return "OK"
    return jsonify(instructions)
@index.route("/test")
def test():
    return redirect("/")


