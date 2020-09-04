from flask import request, json, Response, Blueprint, g, jsonify
from ..models.Campaign import Campaign, CampaignSchema



campaign_api = Blueprint('campaigns_api', __name__)
campaign_schema = CampaignSchema()

@campaign_api.route('/', methods=['POST'])
def create():
  req_data = request.get_json()
  data = campaign_schema.load(req_data)
  # data, error = campaign_schema.load(req_data)
  error = None
  if error: 
    return custom_response(error, 400)

  # import code
  # code.interact(local=dict(globals(), **locals()))

  campaign = Campaign(data)
  campaign.save() 

  campaign_data = campaign_schema.dump(campaign)
  

  return custom_response(campaign_data, 201)
  

def custom_response(res, status_code):
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )


@campaign_api.route('/<int:campaign_id>/', methods=['GET'])
def get_a_campaign(campaign_id):
  campaign = Campaign.get_one_campaign(campaign_id)
  if not campaign: 
    return custom_response({'error':'Campaign not found'}, 404)

  campaign_data = campaign_schema.dump(campaign).data
  return custom_response(campaign_data, 200)

@campaign_api.route('/<int:campaign_id>', methods=['PUT'])
def update(campaign_id):
  req_data = request.get_json()
  data, error = campaign_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  
  campaign = Campaign.get_one_campaign(campaign_id)
  campaign.update(data)
  campaign_data = campaign_schema.dump(campaign).data
  return custom_response(campaign_data, 200)

@campaign_api.route('/<int:campaign_id>', methods=["DELTE"])
def delete(campaign_id):
  campaign = Campaign.get_one_campaign(campaign_id)
  campaign_data = campaign_data.dump(campaign).data
  return custom_response(campaign_data, 200)


@campaign_api.route('/', methods=['GET'])
def get_all_campaigns():
  campaigns = Campaign.get_all_campaigns()

  if not campaigns:
    return custom_response({'error': 'No Campaigns'}, 404)

  # campaign_data = campaign_schema.dump(campaigns)
  campaign_data = []
  for campaign in campaigns:
    campaign_data.append(campaign_schema.dump(campaign))

  return custom_response(campaign_data, 200)
