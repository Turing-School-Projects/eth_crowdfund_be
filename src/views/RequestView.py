from flask import request, json, Response, Blueprint, g, jsonify
from ..models.Request import Request, RequestSchema


request_api = Blueprint('requests_api', __name__)
request_schema = RequestSchema()

def custom_response(res, status_code):
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

@request_api.route('/', methods=['POST'])
def create():
  req_data = request.get_json()
  data = request_schema.load(req_data)
  # data, error = campaign_schema.load(req_data)
  # BUT WITH ERROR: the above code threw an error, currently ignoring errors
  error = None
  if error:
    return custom_response(error, 400)

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