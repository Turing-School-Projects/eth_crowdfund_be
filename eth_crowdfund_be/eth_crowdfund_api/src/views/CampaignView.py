from flask import request, json, Response, Blueprint, g
from ..models.Campaign import Campaign, CampaignSchema

campaign_api = Blueprint('campaigns_api', __name__)
campaign_schema = CampaignSchema()

@campaign_api.route('/', methods=['POST'])
def create():
  req_data = request.get_json()
  print('!-! req_data: {}'.format(req_data))
  data = campaign_schema.load(req_data)
  print('!-! data: {}'.format(data))
  # data, error = campaign_schema.load(req_data)
  error = None
  if error: 
    return custom_response(error, 400)

  # check if campaign already exists
  # campaign_in_db = Campaign.get_campaign_by_name(data.get('name'))
  # if campaign_in_db:
  #   message = {'error': 'Campaign name already in database'}
  #   return custom_response(message, 400)
  campaign = Campaign(data)
  print('!-! campaign: {}'.format(campaign))
  campaign.save() 

  campaign_data = campaign_schema.dump(campaign).data

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
  campaign = Campaign.get_on_campaign(campaign_id)
  campaign_data = campaign_data.dump(campaign).data
  return custom_response(campaign_data, 200)


@campaign_api.route('/all', methods=['GET'])
def get_all_campaigns():
  campaigns = Campaign.get_all_campaigns()
  if not campaigns:
    return custom_response({'error': 'No Campaigns'}, 404)

  campaign_data = campaign_schema.dump(campaigns).data
  return custom_response(campaign_data, 200)
