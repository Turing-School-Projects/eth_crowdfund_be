from flask import request, json, Response, Blueprint, jsonify
from ..models.Campaign import Campaign, CampaignSchema
from ..models.Contributor import Contributor, ContributorSchema
from marshmallow import ValidationError
from sqlalchemy import exc
from . import custom_response


campaign_api = Blueprint('campaigns_api', __name__)
campaign_schema = CampaignSchema()

@campaign_api.route('/hello', methods=['GET'])
def hello():
  return custom_response({"message":"hello"})

@campaign_api.route('/', methods=['POST'])
def create():
  try:
    req_data = request.get_json()
    data = campaign_schema.load(req_data)
  except ValidationError as err:
    return custom_response(err.messages, 400)
  except:
    return custom_response({ "error": "No input data provided" }, 400)

  campaign = Campaign(data)
  campaign.save()
  campaign_data = campaign_schema.dump(campaign)
  return custom_response(campaign_data, 201)

@campaign_api.route('/<int:campaign_id>', methods=['GET'])
def get_a_campaign(campaign_id):
  campaign = Campaign.get_one_campaign(campaign_id)
  if campaign is None:
    return custom_response({'error':'Campaign not found'}, 404)

  campaign_data = campaign_schema.dump(campaign)
  return custom_response(campaign_data, 200)

@campaign_api.route('/<int:campaign_id>', methods=['PUT'])
def update(campaign_id):
  try:
    req_data = request.get_json()
    data = campaign_schema.load(req_data, partial=True)
    campaign = Campaign.get_one_campaign(campaign_id)
    campaign.update(data)
  except ValidationError as err:
    return custom_response(err.messages, 400)
  except exc.IntegrityError as err:
    return custom_response({ "error": err.orig.diag.message_detail}, 400)
  except:
    return custom_response({ "error": "No input data provided" }, 400)

  campaign_data = campaign_schema.dump(campaign)
  return custom_response(campaign_data, 200)


@campaign_api.route('/<int:campaign_id>', methods=["DELETE"])
def delete(campaign_id):
  campaign = Campaign.get_one_campaign(campaign_id)

  if campaign is None:
    return custom_response({ 'error': 'Campaign not found'}, 404)

  campaign.delete()
  campaign_data = campaign_schema.dump(campaign)
  return custom_response(campaign_data, 200)

@campaign_api.route('/', methods=['GET'])
def get_all_campaigns():
  campaigns = Campaign.get_all_campaigns()

  if campaigns is None:
    return custom_response({'error': 'No Campaigns found'}, 404)

  campaign_data = []
  for campaign in campaigns:
    campaign_data.append(campaign_schema.dump(campaign))
  return custom_response(campaign_data, 200)

@campaign_api.route('/manager/<manager>', methods=['GET'])
def get_campaigns_by_manager(manager):
  campaigns = Campaign.get_campaigns_by_manager(manager)
  campaign_data = []
  for campaign in campaigns:
    campaign_data.append(campaign_schema.dump(campaign))
  if campaign_data == []:
    return custom_response({'error': 'The entered manager has no campaigns'}, 404)
  else:
    return custom_response(campaign_data, 200)

@campaign_api.route('/<campaign_address>/contributor/<contributor_address>', methods=['POST'])
def add_contributor_to_campaign(campaign_address, contributor_address):
  try:
    campaign = Campaign.get_campaign_by_address(campaign_address).first()
    contributor = Contributor.get_contributor_by_address(contributor_address).first()
    if contributor == None:
        contributor = Contributor({"address": contributor_address})
        contributor.save()
    campaign.contributors.append(contributor)
    campaign.save()
  except ValidationError as err:
    return custom_response(err.messages, 400)
  except exc.IntegrityError as err:
    return custom_response({ "error": err.orig.diag.message_detail}, 400)
  except:
    return custom_response({ "error": "The entered campaign address and/or contributor address are incorrect" }, 400)

  campaign_data = campaign_schema.dump(campaign)
  return custom_response(campaign_data, 201)


