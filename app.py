from os import error
from flask import Flask, json, jsonify

app = Flask(__name__)

from monedas import monedas

@app.route('/ping')
def ping():
    return jsonify({"massage": "pong!"})

@app.route('/monedas')
def getMonedas():
    return jsonify({"monedas": monedas, "message": "Monedas lista"})

@app.route('/monedas/<string:moneda_name>')
def getMoneda(moneda_name):
    monedasFound = [moneda for moneda in monedas if moneda['name'] == moneda_name]
    if (len(monedasFound) > 0):
        return jsonify({"moneda": monedasFound[0]})
    return jsonify({"message": "Product not found 404 "})

if __name__ == '__main__':
    app.run(debug=True, port=4000)