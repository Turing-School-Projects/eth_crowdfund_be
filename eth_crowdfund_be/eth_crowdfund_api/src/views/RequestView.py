from flask import request, json, Response, Blueprint, g, jsonify
from ..models.Campaign import Campaign, CampaignSchema
from ..models.Request import Request, RequestSchema


request_api = Blueprint('requests_api', __name__)
request_schema = RequestSchema()

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


def custom_response(res, status_code):
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

@request_api.route('/', methods=['GET'])
def get_all_requests():
  requests = Request.get_all_requests()

  if not requests:
    return custom_response({'error': 'No Requests'}, 404)

  request_data = []
  for request in requests:
    request_data.append(request_schema.dump(request))
  return custom_response(request_data, 200)
