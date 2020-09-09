from flask import request, json, Response, Blueprint, jsonify 
from ..services.ConversionService import ConversionService
import requests

price_converter_api = Blueprint('price_converter_api', __name__)

@price_converter_api.route('/', methods=['GET'])
def eth_to_usd(): 
    wei = float(request.args['wei'])
    conversion_service = ConversionService()
    value_in_usd = conversion_service.wei_to_usd(wei)
    return jsonify(USD=value_in_usd)