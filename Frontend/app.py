from flask import Flask
from flask import request, redirect, render_template, session
import requests
import base64
import requests

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("home.html")


@app.route('/pipe', methods=["GET", "POST"])
def pipe():
    data = request.form.get("data")
    payload = {}
    headers = {}
    url = "http://backend:4000/autocomplete?query=" + str(data)
    print('urll iss.....', url)
    response = requests.request("GET", url, headers=headers, data=payload)
    print('response is.......', response)
    #es = response.json()
    # val= es['hits']['hits'][0]['_source']
    #  print(val)
    return response.json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
