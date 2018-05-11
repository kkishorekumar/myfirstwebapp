from flask import Flask, render_template, jsonify, request
import re
import os

app =Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/tst/',methods=["GET"])
def geti():
    resp = {"username": "kkk"}
    return jsonify(resp)

@app.route('/chk/',methods=["POST"])
def posti():
    req = request.json
    for header in req:
        if header == "queryResult":
            for item in req[header]:
                if item == "intent":
                    for option in req[header][item]:
                        if option == "displayName":
                            if req[header][item][option] == "askmobile":
                                for itm in req[header]:
                                    if itm == "outputContexts":
                                        for para in req[header][itm][len(req[header][itm])-1]:
                                            if para == "parameters":
                                                for mob in req[header][itm][len(req[header][itm])-1][para]:
                                                    if mob == "mobileNumber":
                                                        p = re.compile(r'^[6789]\d{9}$',re.I|re.M)
                                                        print (req[header][itm][len(req[header][itm])-1][para][mob])
                                                        mobil = (req[header][itm][len(req[header][itm])-1][para][mob])
                                                        if p.match(str(req[header][itm][len(req[header][itm])-1][para][mob])):
                                                            respo = {"fulfillmentText": "Please enter the OTP received","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {"name":"otpevent","languageCode":"en-IN","parameters":{"mobileNumber":str(mobil)}}}
                                                            return jsonify(respo)
                                                        else:
                                                            respo = {"fulfillmentText": "Please enter a valid 10 digit mobile","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {"name":"mobevent","languageCode":"en-IN","parameters":{"mobileNumber":str(mobil)}}}
                                                            return jsonify(respo)
                            elif req[header][item][option] == "askotp":
                                for itm in req[header]:
                                    if itm == "outputContexts":
                                        for para in req[header][itm][len(req[header][itm])-1]:
                                            if para == "parameters":
                                                for mob in req[header][itm][len(req[header][itm])-1][para]:
                                                    if mob == "otp":
                                                        p = re.compile(r'^\d{6}$',re.I|re.M)
                                                        print (req[header][itm][len(req[header][itm])-1][para][mob])
                                                        otpi = (req[header][itm][len(req[header][itm])-1][para][mob])
                                                        if p.match(str(req[header][itm][len(req[header][itm])-1][para][mob])):
                                                            respo = {"fulfillmentText": "","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {"name":"otpevent","languageCode":"en-IN","parameters":{"otp":str(otpi)}}}
                                                            return jsonify(respo)
                                                        else:
                                                            respo = {"fulfillmentText": "Please enter a valid 6 digit OTP","fulfillmentMessages": [],"source": "example.com","payload": {},"outputContexts": [ ],"followupEventInput": {"name":"otpevent","languageCode":"en-IN","parameters":{"otp":str(otpi)}}}
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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
