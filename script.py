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
    for header in req:
        if header == "queryResult":
            for item in req[header]:
                if item == "intent":
                    for option in req[header][item]:
                        if option == "displayName":
                            if req[header][item][option] == "SharingMobile":
                                for itm in req[header]:
                                    if itm == "parameters":
                                        for para in req[header][itm]:
                                            if para == "mobilenumber":
                                                p = re.compile(r'^[6789]\d{9}$',re.I|re.M)
                                                #print (req[header][itm][para])
                                                if p.match(str(req[header][itm][para])):
                                                    respo = {"fulfillmentText": "Please enter the OTP received","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {}}
                                                    return jsonify(respo)
                                                else:
                                                    respo = {"fulfillmentText": "Please enter a valid 10 digit mobile","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {}}
                                                    return jsonify(respo)
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
