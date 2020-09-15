from flask import request, json, Response, Blueprint, g, jsonify
from marshmallow import ValidationError
from sqlalchemy import exc
from ..models.Request import Request, RequestSchema
from ..models.Campaign import Campaign, CampaignSchema
from . import custom_response
from ..mailers.mailer import request_notification

request_api = Blueprint('requests_api', __name__)
request_schema = RequestSchema()

@request_api.route('/', methods=['POST'])
def create():
  
  try: 
    req_data = request.get_json()
    # get number of campaign requests
    campaign = Campaign.get_one_campaign(req_data['campaign_id'])
    req_data['eth_id'] = len(campaign.requests)
    data = request_schema.load(req_data)
  except ValidationError as err:
    return custom_response(err.messages, 400)
  except:  
    return custom_response({ "error": "No input data provided" }, 400)

  request_info = Request(data)
  request_info.save()

  emails = [contributor.email for contributor in campaign.contributors]
  if len(emails) > 0: 
    request_notification(emails, campaign.name)

  request_data = request_schema.dump(request_info)
  return custom_response(request_data, 201)

@request_api.route('/', methods=['GET'])
def get_all_requests():
  requests = Request.get_all_requests()

  if requests is None:
    return custom_response({'error': 'No Requests found'}, 404)

  request_data = []
  for campaign_request in requests:
    request_data.append(request_schema.dump(campaign_request))
  return custom_response(request_data, 200)

@request_api.route('/<int:request_id>', methods=['GET'])
def get_a_request(request_id):
  campaign_request = Request.get_one_request(request_id)
  if campaign_request is None:
    return custom_response({ 'error': 'Request not found'}, 404)
  
  campaign_request_data = request_schema.dump(campaign_request)
  return custom_response(campaign_request_data, 200)

@request_api.route('/<int:request_id>', methods=['PUT'])
def update(request_id):

  try: 
    req_data = request.get_json()
    data = request_schema.load(req_data, partial=True)
    campaign_request = Request.get_one_request(request_id)
    campaign_request.update(data)
  except ValidationError as err:
    return custom_response(err.messages, 400)
  except exc.IntegrityError as err: 
    return custom_response({ "error": err.orig.diag.message_detail }, 400)
  except:  
    return custom_response({ "error": "No input data provided" }, 400)

  request_data = request_schema.dump(campaign_request)
  return custom_response(request_data, 200)

@request_api.route('/<int:request_id>', methods=['DELETE'])
def delete(request_id):
  campaign_request = Request.get_one_request(request_id)

  if campaign_request is None: 
    return custom_response({ 'error': 'Request not found'}, 404)

  campaign_request.delete()
  campaign_request_data = request_schema.dump(campaign_request)
  return custom_response(campaign_request_data, 200)