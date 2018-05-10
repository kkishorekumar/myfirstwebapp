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
    respo = request.json
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
