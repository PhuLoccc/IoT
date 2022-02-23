import sys
sys.path.append('pages')
from OpenSSL import SSL
from flask import Flask, render_template
from index import index
app = Flask(__name__,static_folder="Web",template_folder="Web/templates",static_url_path="")
app.register_blueprint(index, url_prefix = "/")

if __name__ == "__main__":
    # app.run(host="172.16.1.27", port=80, ssl_context=('cert.pem', 'key.pem'))
    app.run(host="192.168.1.8", port=80)