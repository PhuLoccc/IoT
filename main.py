import sys
sys.path.append('C:\\Users\\ASUS\\Desktop\\IoT\\pages')
from flask import Flask, render_template

from index import index
app = Flask(__name__,static_folder="Web",template_folder="Web/templates",static_url_path="")
app.register_blueprint(index, url_prefix = "/")

if __name__ == "__main__":
    app.run(host="192.168.0.101", port=80)