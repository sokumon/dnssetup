from flask import Flask,render_template,request
import json
import requests 
base_url = "https://api.name.com/v4/"
dev_token = "f7ac9b9722932715b0db9a293740a7f42218b45e"
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

# @app.post('/setdns')
# def setdns():


@app.post('/setdns')
def setdns():
    host = request.form["host"]
    dnstype = request.form["type"]
    answer = request.form["answer"]
    ttl = request.form["ttl"]

    headers = {
    'Content-Type': 'application/json',
    }

    json_data = {
    'host': host,
    'type': dnstype,
    'answer': answer,
    'ttl': ttl,
    }

    response = requests.post(
    'https://api.dev.name.com/v4/domains/atharvadhamankar.engineer/records',
    headers=headers,
    json=json_data,
    auth=('AtharvaDhamankar-test', dev_token),
    )
    print(response.json())
    return "Success"


app.run()