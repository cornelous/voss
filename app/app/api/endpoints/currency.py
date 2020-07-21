
import os
import requests
from flask import Flask, make_response, render_template, request, jsonify, json
from ...main import app

baseAPIURL = os.environ.get("API_URL", default="http://api.openrates.io/")

@app.route("/currencies/")
def route_currencies():       
    # grab base and target currency from URL
    base = request.args.get('base')
    target = request.args.get('target')

    # ensure that base and target are from [ZAR, USD, EUR, GBP]
    allowedCurrencies = ['ZAR', 'USD', 'EUR', 'GBP']
    
    if base not in allowedCurrencies :
        return base + " is not supported as a currency"
        
    if target not in allowedCurrencies :
        return target + " is not supported as a currency"

    if (base == 'EUR') and (target == 'EUR'):
        return "Conversion from " + base + " to " + base + " is not supported" 

    getZAREquivalent = baseAPIURL + "latest?symbols="+ target + "&base=" + base
    ZAREquivalent = requests.get(getZAREquivalent)
    r = ZAREquivalent.json()

    targetEquiv = r["rates"].get(target)
    app.logger.debug("Converted " + base + " to " + target + " and " + target + " value was " + str(targetEquiv) )
    return jsonify(targetEquiv)