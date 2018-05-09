from flask import Flask, render_template, jsonify, request
import re

app =Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/ome/',methods=["GET"])
def geti():
    resp = {"username": "kkk"}
    return jsonify(resp)

@app.route('/ost/',methods=["POST"])
def posti():
    responseId = request.json["responseId"]
    req = request.json
    respo = {"fulfillmentText": "","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {}}
    return jsonify(respo)

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/policy/')
def policy():
    return render_template("policy.html")

if __name__ == "__main__":
    app.run(debug=True)
