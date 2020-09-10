from flask import request, json, Response, Blueprint, g, jsonify
from marshmallow import ValidationError
from sqlalchemy import exc
from ..models.Contributor import Contributor, ContributorSchema
from . import custom_response


contributor_api = Blueprint('contributor_api', __name__)
contributor_schema = ContributorSchema()

@contributor_api.route('/', methods=['POST'])
def create():
  try:
    input_data = request.get_json()
    data = contributor_schema.load(input_data)
  except ValidationError as err:
    return custom_response(err.messages, 400)
  except:
    return custom_response({ "error": "No input data provided" }, 400)

  contributor_info = Contributor(data)
  contributor_info.save()
  contributor_data = contributor_schema.dump(contributor_info)
  return custom_response(contributor_data, 201)

# @request_api.route('/', methods=['GET'])
# def get_all_requests():
#   requests = Request.get_all_requests()
#
#   if requests is None:
#     return custom_response({'error': 'No Requests found'}, 404)
#
#   request_data = []
#   for campaign_request in requests:
#     request_data.append(request_schema.dump(campaign_request))
#   return custom_response(request_data, 200)
#
# @request_api.route('/<int:request_id>', methods=['GET'])
# def get_a_request(request_id):
#   campaign_request = Request.get_one_request(request_id)
#   if campaign_request is None:
#     return custom_response({ 'error': 'Request not found'}, 404)
#
#   campaign_request_data = request_schema.dump(campaign_request)
#   return custom_response(campaign_request_data, 200)
#
@contributor_api.route('/<int:contributor_id>', methods=['PUT'])
def update(contributor_id):

  try:
    input_data = request.get_json()
    data = contributor_schema.load(input_data, partial=True)
    contributor_request = Contributor.get_one_contributor(contributor_id)
    contributor_request.update(data)
  except ValidationError as err:
    return custom_response(err.messages, 400)
  except exc.IntegrityError as err:
    return custom_response({ "error": err.orig.diag.message_detail }, 400)
  except:
    return custom_response({ "error": "No input data provided" }, 400)

  output_data = contributor_schema.dump(contributor_request)
  return custom_response(output_data, 200)
#
# @request_api.route('/<int:request_id>', methods=['DELETE'])
# def delete(request_id):
#   campaign_request = Request.get_one_request(request_id)
#
#   if campaign_request is None:
#     return custom_response({ 'error': 'Request not found'}, 404)
#
#   campaign_request.delete()
#   campaign_request_data = request_schema.dump(campaign_request)
#   return custom_response(campaign_request_data, 200)
