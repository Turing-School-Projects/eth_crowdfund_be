from flask import request, json, Response, Blueprint, g, jsonify
from marshmallow import ValidationError
from sqlalchemy import exc
from ..models.Contributor import Contributor, ContributorSchema
from ..models.Campaign import Campaign, CampaignSchema
from . import custom_response


contributor_api = Blueprint('contributor_api', __name__)
contributor_schema = ContributorSchema()
campaign_schema = CampaignSchema()

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

@contributor_api.route('/<contributor_address>/campaigns', methods=['GET'])
def get_campaigns(contributor_address):
  try:
    contributor = Contributor.get_contributor_by_address(contributor_address).first()
  except ValidationError as err:
    return custom_response(err.messages, 400)
  except exc.IntegrityError as err:
    return custom_response({ "error": err.orig.diag.message_detail }, 400)
  except:
    return custom_response({ "error": "No input data provided" }, 400)
  campaigns = contributor.contributions
  output_data = []
  for campaign in campaigns:
      output_data.append(campaign_schema.dump(campaign))
  return custom_response(output_data, 200)
