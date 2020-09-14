from ..models import db
from ..models.Campaign import Campaign
from ..models.Request import Request
from ..models.Contributor import Contributor
from ..models.CampaignContributor import CampaignContributor
from ..models.ApiKey import ApiKey
 
def add_seeds():
 
    print('Seeding...')
 
    #  Campaign Seeds
    campaign1 = {
       'name': 'Build a Well',
       'description': 'A small town in South Africa needs a well for clean water',
       # Uses lorem picsum for random pics
       'image': 'https://picsum.photos/200/300',
       # Manager is a random string
       'manager': 'X5JT498FJeklnsd8382hf',
       'upvote': 50,
       'min_contribution': 1.5,
       # Address is a random string
       'address': 'FjSDh482hfjGE77dk',
       'expiration': '10/25/2020'
    }
 
    campaign2 = {
       'name': 'Market St. Soup Kitchen',
       'description': 'Need help serving community',
       # Uses lorem picsum for random pics
       'image': 'https://picsum.photos/200/300',
       # Manager is a random string
       'manager': 'LJHhf82u3hr0d9uhUg4g',
       'upvote': 50,
       'min_contribution': 1.5,
       # Address is a random string
       'address': 'Hf84jhGE9fdjF9ehfdse45',
       'expiration': '10/25/2020'
    }
 
    campaign3 = {
       'name': 'Arc Thrift',
       'description': 'Serving communities hit hard by Covid19',
       # Uses lorem picsum for random pics
       'image': 'https://picsum.photos/200/300',
       # Manager is a random string
       'manager': 'jhF8dfh4jjgfdkjs45',
       'upvote': 50,
       'min_contribution': 1.5,
       # Address is a random string
       'address': 'DFjh489GD74hgls8',
       'expiration': '10/25/2020'
    }
 
    request1= {
       'campaign_id': 0,
       'description': 'Buy supplies',
       'image': 'https://picsum.photos/200/300',
       'value': 100,
       'recipient': 'kfh7DFh38H',
       'approvals': 0,
 
    }
 
    request2= {
       'campaign_id': 0,
       'description': 'Lunch for volunteers',
       'image': 'https://picsum.photos/200/300',
       'value': 250,
       'recipient': 'JHh7734utg8ds7H',
       'approvals': 0,
 
    }
 
    request3= {
       'campaign_id': 0,
       'description': 'Cleaning supplies',
       'image': 'https://picsum.photos/200/300',
       'value': 25,
       'recipient': 'jhF97hdfha97',
       'approvals': 0,
 
    }
 
    contributor1 = {
       "address": "Fj408adfH0ih",
       "email": "test1@email.com"
    }
 
    contributor2 = {
       "address": "lkFh84hDfh98",
       "email": "test2@email.com"
    }
 
    contributor3 = {
       "address": "H39ghd8yaG",
       "email": "test3@email.com"
    }
 
    campaign_contributor1 = {
       "campaign_id": 0,
       "contributor_id": 0,
       "value": 50
    }
 
    campaign_contributor2 = {
       "campaign_id": 0,
       "contributor_id": 0,
       "value": 50
     }
 
    campaign_contributor3 = {
       "campaign_id": 0,
       "contributor_id": 0,
       "value": 50
    }

    api_key_admin = {
      "key": "macbeth",
      "email": "admin@ethoboost.com"
    }
 
    # Deletes all rows in Campaign Table
    db.session.query(CampaignContributor).delete()
    db.session.query(Contributor).delete()
    db.session.query(Request).delete()
    db.session.query(Campaign).delete()
    db.session.query(ApiKey).delete()
    
    # Campaigns
    campaign_list = [Campaign(campaign1), Campaign(campaign2), Campaign(campaign3)]
    db.session.add_all(campaign_list)
    campaign_ids = db.session.query(Campaign.id).all()
    campaign_ids = [r[0] for r in campaign_ids]

    # Requests
    request1['campaign_id'] = campaign_ids[0]
    request2['campaign_id'] = campaign_ids[0]
    request3['campaign_id'] = campaign_ids[1]
    request1['eth_id'] = 0
    request2['eth_id'] = 1
    request3['eth_id'] = 0
    
    request_list = [Request(request1), Request(request2), Request(request3)]
    db.session.add_all(request_list)
    
    # Contributors
    contributor_list = [Contributor(contributor1), Contributor(contributor2), Contributor(contributor3)]
    db.session.add_all(contributor_list)
    contributor_ids = db.session.query(Contributor.id).all()
    contributor_ids = [r[0] for r in contributor_ids]
    
    # Campaign Contributors
    campaign_contributor1['campaign_id'] = campaign_ids[0]
    campaign_contributor2['campaign_id'] = campaign_ids[0]
    campaign_contributor3['campaign_id'] = campaign_ids[1]
    campaign_contributor1['contributor_id'] = contributor_ids[0]
    campaign_contributor2['contributor_id'] = contributor_ids[0]
    campaign_contributor3['contributor_id'] = contributor_ids[1]
    
    campaign_contributor_list = [CampaignContributor(campaign_contributor1), CampaignContributor(campaign_contributor2), CampaignContributor(campaign_contributor3)]
    db.session.add_all(campaign_contributor_list)

    # ApiKeys
    api_key_list = [ApiKey(api_key_admin)]
    db.session.add_all(api_key_list)
    db.session.commit(),
    
    print('Finished Seeding')
    return
    

