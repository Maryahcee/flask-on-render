from flask import Flask, request
from flask_cors import CORS

import requests

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

SHORTEN_BASE_URL = "https://cleanuri.com/api/v1/shorten"


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/shorten-url',methods=["POST"])
def shorten_url():
    url_to_shorten = request.json["url"]
    shorten_call = requests.post(
        SHORTEN_BASE_URL,
        json={"url":url_to_shorten}
    )
    return shorten_call.json()

if __name__ == "__main__":
   app.run(port=8000)