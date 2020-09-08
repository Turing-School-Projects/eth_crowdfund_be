from flask import request, json, Response, Blueprint, jsonify 
import requests

price_converter_api = Blueprint('price_converter_api', __name__)

@price_converter_api.route('/', methods=['GET'])
def eth_to_usd(): 
    eth_amount = float(request.args['eth'])
    response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD')
    conversion_rate = response.json()['USD'] 
    value_in_usd = eth_amount * conversion_rate
    return jsonify(value=value_in_usd)