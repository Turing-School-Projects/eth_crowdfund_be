import pdb
import unittest
import os
import json
# import flask_sqlalchemy
from ..models.Campaign import Campaign
from ..models.Request import Request
from ..app import create_app, db

def func(x):
  return x + 1
# basic test
def test_answer():
  assert func(3) == 4

class RequestTest(unittest.TestCase):
  # set up the tests with 2 campaigns
  # This runs before EVERY test. not once before all
  def setUp(self):
    self.app = create_app('testing')
    self.client = self.app.test_client
    self.campaign1 = {
        'name': 'Build a Well',
        'description': 'A small town in South Africa needs a well for clean water',
        'image': 'https://picsum.photos/200/300',
        'manager': 'X5JT498FJeklnsd8382hf',
        'contributors': 25,
        'upvote': 50,
        'min_contribution': 1.5,
        'address': 'FjSDh482hfjGE77dk',
    }

    self.campaign2 = {
        'name': 'Market St. Soup Kitchen',
        'description': 'Need help serving community',
        'image': 'https://picsum.photos/200/300',
        'manager': 'LJHhf82u3hr0d9uhUg4g',
        'contributors': 25,
        'upvote': 50,
        'min_contribution': 1.5,
        'address': 'Hf84jhGE9fdjF9ehfdse45',
    }

    self.request1= {
        'campaign_id': 0,
        'description': 'Buy supplies',
        'image': 'https://picsum.photos/200/300',
        'value': 100,
        'recipient': 'kfh7DFh38H',
        'approvals': 0,

    }

    self.request2= {
        'campaign_id': 0,
        'description': 'Lunch for volunteers',
        'image': 'https://picsum.photos/200/300',
        'value': 250,
        'recipient': 'JHh7734utg8ds7H',
        'approvals': 0,

    }

    self.request3= {
        'campaign_id': 0,
        'description': 'Cleaning supplies',
        'image': 'https://picsum.photos/200/300',
        'value': 25,
        'recipient': 'jhF97hdfha97',
        'approvals': 0,

    }


    with self.app.app_context():
      # create all db objects
      db.create_all()
      # delete test campaigns by name
      existing_campaign1 = Campaign.get_campaign_by_name(self.campaign1["name"])
      if existing_campaign1:
        existing_campaign1.delete()
      existing_campaign2 = Campaign.get_campaign_by_name(self.campaign2["name"])
      if existing_campaign2:
        existing_campaign2.delete()

  def test_request_creation(self):
    # send a request
    res = self.client().post('/api/v1/campaigns/',
                              headers={'Content-Type': 'application/json'},
                              data=json.dumps(self.campaign1))
    self.assertEqual(res.status_code, 201)
    campaign_id = json.loads(res.data)["id"]

    request = {
        'campaign_id': campaign_id,
        'description': 'Buy supplies',
        'image': 'https://picsum.photos/200/300',
        'value': 100,
        'recipient': 'kfh7DFh38H',
        'approvals': 0,

    }

    res = self.client().post('/api/v1/requests/',
                              headers={'Content-Type': 'application/json'},
                              data=json.dumps(request))
    self.assertEqual(res.status_code, 201)
    json_data = json.loads(res.data)

    self.assertEqual(request["campaign_id"], json_data["campaign_id"])

  # def test_campaign_update(self):
  #   campaign1_update = {
  #     "description": "new description",
  #     "contributors": 5,
  #     "manager": "1x3y"
  #   }
  #   # create the campaign before updating
  #   res = self.client().post('/api/v1/campaigns/',
  #                            headers={'Content-Type': 'application/json'},
  #                            data=json.dumps(self.campaign1))
  #   self.assertEqual(res.status_code, 201)
  #   campaign1_id = json.loads(res.data)["id"]
  #   # save the id and update campaign
  #   res_update = self.client().put('/api/v1/campaigns/{}'.format(campaign1_id),
  #                           headers={'Content-Type': 'application/json'},
  #                           data=json.dumps(campaign1_update))
  #
  #   json_data = json.loads(res_update.data)
  #   self.assertEqual(self.campaign1["name"], json_data["name"])
  #   self.assertNotEqual(self.campaign1["description"], json_data["description"])
  #   self.assertEqual(campaign1_update["description"], json_data["description"])
  #   self.assertNotEqual(self.campaign1["contributors"], json_data["contributors"])
  #   self.assertEqual(campaign1_update["contributors"], json_data["contributors"])
  #   self.assertNotEqual(self.campaign1["manager"], json_data["manager"])
  #   self.assertEqual(campaign1_update["manager"], json_data["manager"])
  #   self.assertEqual(res_update.status_code, 200)
  #
  # def test_delete(self):
  #   res = self.client().post('/api/v1/campaigns/',
  #                             headers={'Content-Type': 'application/json'},
  #                             data=json.dumps(self.campaign1))
  #   self.assertEqual(res.status_code, 201)
  #   campaign1_id = json.loads(res.data)["id"]
  #
  #   # delete campaign
  #   res_delete = self.client().delete('/api/v1/campaigns/{}'.format(campaign1_id), headers={'Content-Type': 'application/json'})
  #   self.assertEqual(res_delete.status_code, 200)
  #
  # def test_get_all_campaigns(self):
  #   # create 2 campaigns
  #   res1 = self.client().post('/api/v1/campaigns/',
  #                            headers={'Content-Type': 'application/json'},
  #                            data=json.dumps(self.campaign1))
  #   self.assertEqual(res1.status_code, 201)
  #   res2 = self.client().post('/api/v1/campaigns/',
  #                            headers={'Content-Type': 'application/json'},
  #                            data=json.dumps(self.campaign2))
  #   self.assertEqual(res2.status_code, 201)
  #
  #
  #   res_index = self.client().get('/api/v1/campaigns/',
  #                  headers={'Content-Type': 'application/json'})
  #   json_data = json.loads(res_index.data)
  #   self.assertEqual(len(json_data), 2)
  #   self.assertEqual(res_index.status_code, 200)
  #
  # def test_get_one_campaign(self):
  #   # create 2 campaigns
  #   res1 = self.client().post('/api/v1/campaigns/',
  #                            headers={'Content-Type': 'application/json'},
  #                            data=json.dumps(self.campaign1))
  #   self.assertEqual(res1.status_code, 201)
  #   campaign1_id = json.loads(res1.data)["id"]
  #
  #   res2 = self.client().post('/api/v1/campaigns/',
  #                            headers={'Content-Type': 'application/json'},
  #                            data=json.dumps(self.campaign2))
  #   self.assertEqual(res2.status_code, 201)
  # # GETTING A `308 Redirect` error. not sure why. works correctly on postman
  #   res_show = self.client().get('/api/v1/campaigns/{}'.format(campaign1_id),
  #                                headers={'Content-Type': 'application/json'})
  #   self.assertEqual(res_show.status_code, 200)
  #   json_data = json.loads(res_show.data)
  #   self.assertEqual(self.campaign1["name"], json_data["name"])
  #   self.assertNotEqual(self.campaign2["name"], json_data["name"])
  #   self.assertEqual(self.campaign1["description"], json_data["description"])
  #   self.assertNotEqual(self.campaign2["description"], json_data["description"])
  #   self.assertEqual(self.campaign1["manager"], json_data["manager"])
  #   self.assertNotEqual(self.campaign2["manager"], json_data["manager"])
  #   self.assertEqual(self.campaign1["address"], json_data["address"])
  #   self.assertEqual(self.campaign1["min_contribution"], json_data["min_contribution"])
  #   self.assertNotEqual(self.campaign2["min_contribution"], json_data["min_contribution"])
  #
  # def test_campaigns_by_manager(self):
  #   # create 2 campaigns
  #   res1 = self.client().post('/api/v1/campaigns/',
  #                            headers={'Content-Type': 'application/json'},
  #                            data=json.dumps(self.campaign1))
  #   self.assertEqual(res1.status_code, 201)
  #   res2 = self.client().post('/api/v1/campaigns/',
  #                            headers={'Content-Type': 'application/json'},
  #                            data=json.dumps(self.campaign2))
  #   self.assertEqual(res2.status_code, 201)
  #
  #
  #   res_index = self.client().get('/api/v1/campaigns/manager/13',
  #                  headers={'Content-Type': 'application/json'},
  #                  )
  #
  #   self.assertEqual(res_index.status_code, 200)
  #   json_data = json.loads(res_index.data)
  #
  #   self.assertEqual(len(json_data), 1)
  #   self.assertEqual(self.campaign2["name"], json_data[0]["name"])
  #   self.assertEqual(self.campaign2["description"], json_data[0]["description"])
  #   self.assertEqual(self.campaign2["image"], json_data[0]["image"])
  #   self.assertEqual(self.campaign2["contributors"], json_data[0]["contributors"])
  #   self.assertEqual(self.campaign2["upvote"], json_data[0]["upvote"])
  #   self.assertEqual(self.campaign2["manager"], json_data[0]["manager"])
  #   self.assertEqual(self.campaign2["address"], json_data[0]["address"])
  #   self.assertEqual(self.campaign2["min_contribution"], json_data[0]["min_contribution"])
  #
  #   #sad path test
  #   res_index = self.client().get('/api/v1/campaigns/manager/k',
  #                  headers={'Content-Type': 'application/json'},
  #                  )
  #   self.assertEqual(res_index.status_code, 404)
  #   json_data = json.loads(res_index.data)
  #   self.assertEqual("The entered manager has no campaigns", json_data["error"])
