
import os
import sys
import requests
from flask import Flask, make_response, render_template, request, jsonify, json
from ...main import app
from .errors import CurrencyConverterRequestError, CurrencyConverterAPIError

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

    try:
        ZAREquivalent = requests.get(getZAREquivalent)
    except requests.exceptions.RequestException as e:
        exc_info = sys.exc_info()
        # app.logger.error("Failed to make API call with base :" + base + " and target " + target )
        raise CurrencyConverterRequestError(CurrencyConverterRequestError(e), exc_info[2])

    # in case the response you get back is not json
    if not ZAREquivalent.ok:
        if 'application/json' in ZAREquivalent.headers.get('Content-Type'):
            raise CurrencyConverterAPIError(ZAREquivalent.reason,
                                    ZAREquivalent.status_code,
                                    ZAREquivalent.json()
                                    )
        else:
            raise CurrencyConverterRequestError(ZAREquivalent.reason, ZAREquivalent.status_code)

    r = ZAREquivalent.json()

    targetEquiv = r["rates"].get(target)
    app.logger.debug("Converted " + base + " to " + target + " and " + target + " value was " + str(targetEquiv) )
    return jsonify(targetEquiv)