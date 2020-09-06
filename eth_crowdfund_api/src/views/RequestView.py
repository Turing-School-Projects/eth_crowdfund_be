from flask import request, json, Response, Blueprint, g, jsonify
from marshmallow import ValidationError
from ..models.Request import Request, RequestSchema
from . import custom_response


request_api = Blueprint('requests_api', __name__)
request_schema = RequestSchema()

@request_api.route('/', methods=['POST'])
def create():
  try: 
    req_data = request.get_json()
    data = request_schema.load(req_data)
  except ValidationError as err:
    return custom_response(err.messages, 400)
  except:  
    return custom_response({ "error": "No input data provided" }, 400)

  request_info = Request(data)
  request_info.save()
  request_data = request_schema.dump(request_info)
  return custom_response(request_data, 201)

@request_api.route('/', methods=['GET'])
def get_all_requests():
  requests = Request.get_all_requests()

  if not requests:
    return custom_response({'error': 'No Requests'}, 404)

  request_data = []
  for campaign_request in requests:
    request_data.append(request_schema.dump(campaign_request))
  return custom_response(request_data, 200)

@request_api.route('/<int:request_id>', methods=['GET'])
def get_a_request(request_id):
  campaign_request = Request.get_one_request(request_id)
  if not campaign_request:
    return custom_response({ 'error': 'Request not found'}, 404)
  
  campaign_request_data = request_schema.dump(campaign_request)
  return custom_response(campaign_request_data, 200)

@request_api.route('/<int:request_id>', methods=['PUT'])
def update(request_id):
  req_data = request.get_json()
  data = request_schema.load(req_data, partial=True)

  campaign_request = Request.get_one_request(request_id)
  campaign_request.update(data)
  request_data = request_schema.dump(campaign_request)
  return custom_response(request_data, 200)

@request_api.route('/<int:request_id>', methods=['DELETE'])
def delete(request_id):
  campaign_request = Request.get_one_request(request_id)
  campaign_request.delete()
  campaign_request_data = request_schema.dump(campaign_request)
  return custom_response(campaign_request_data, 200)