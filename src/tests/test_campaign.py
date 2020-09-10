import pdb
import unittest
import os
import json
# import flask_sqlalchemy
from ..models.Campaign import Campaign
from ..app import create_app, db

def func(x):
  return x + 1
# basic test
def test_answer():
  assert func(3) == 4

class CampaignTest(unittest.TestCase):
  # set up the tests with 2 campaigns
  # This runs before EVERY test. not once before all
  def setUp(self):
    self.app = create_app('testing')
    self.client = self.app.test_client
    self.campaign1 = {
        "name": "camp",
        "description": "desc1",
        "image": "image.edu",
        "contributors": 1,
        "upvote": 2,
        "manager": "3",
        "address": "4",
        "min_contribution": 5.0
    }
    self.campaign2 = {
        "name": "Eth",
        "description": "desc2",
        "image": "image.com",
        "contributors": 100,
        "upvote": 222,
        "manager": "13",
        "address": "14",
        "min_contribution": 50.2
    }

    with self.app.app_context():
      # create all db objects
      db.drop_all()
      db.create_all()


  def test_campaign_creation(self):
    # send a request
    res = self.client().post('/api/v1/campaigns/',
                              headers={'Content-Type': 'application/json'},
                              data=json.dumps(self.campaign1))
    json_data = json.loads(res.data)
    # check the names. I'd prefer to have a simpler call, but there are a few differences that prevent self.campaign1 == json_data
    self.assertEqual(self.campaign1["name"], json_data["name"])
    self.assertEqual(self.campaign1["description"], json_data["description"])
    self.assertEqual(self.campaign1["image"], json_data["image"])
    self.assertEqual(self.campaign1["contributors"], json_data["contributors"])
    self.assertEqual(self.campaign1["upvote"], json_data["upvote"])
    self.assertEqual(self.campaign1["manager"], json_data["manager"])
    self.assertEqual(self.campaign1["address"], json_data["address"])
    self.assertEqual(self.campaign1["min_contribution"], json_data["min_contribution"])
    # just checking a sad path
    self.assertNotEqual(self.campaign1["min_contribution"], 100)
    self.assertEqual(res.status_code, 201)

  def test_campaign_update(self):
    campaign1_update = {
      "description": "new description",
      "contributors": 5,
      "manager": "1x3y",
      "value": 213.79
    }
    # create the campaign before updating
    res = self.client().post('/api/v1/campaigns/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(self.campaign1))
    self.assertEqual(res.status_code, 201)
    campaign1_id = json.loads(res.data)["id"]
    # save the id and update campaign
    res_update = self.client().put('/api/v1/campaigns/{}'.format(campaign1_id),
                            headers={'Content-Type': 'application/json'},
                            data=json.dumps(campaign1_update))

    json_data = json.loads(res_update.data)
    self.assertEqual(self.campaign1["name"], json_data["name"])
    self.assertNotEqual(self.campaign1["description"], json_data["description"])
    self.assertEqual(campaign1_update["description"], json_data["description"])
    self.assertNotEqual(self.campaign1["contributors"], json_data["contributors"])
    self.assertEqual(campaign1_update["contributors"], json_data["contributors"])
    self.assertNotEqual(self.campaign1["manager"], json_data["manager"])
    self.assertEqual(campaign1_update["manager"], json_data["manager"])
    self.assertEqual(213.79, json_data["value"])
    self.assertEqual(res_update.status_code, 200)

  def test_delete(self):
    res = self.client().post('/api/v1/campaigns/',
                              headers={'Content-Type': 'application/json'},
                              data=json.dumps(self.campaign1))
    self.assertEqual(res.status_code, 201)
    campaign1_id = json.loads(res.data)["id"]

    # delete campaign
    res_delete = self.client().delete('/api/v1/campaigns/{}'.format(campaign1_id), headers={'Content-Type': 'application/json'})
    self.assertEqual(res_delete.status_code, 200)

  def test_get_all_campaigns(self):
    # create 2 campaigns
    res1 = self.client().post('/api/v1/campaigns/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(self.campaign1))
    self.assertEqual(res1.status_code, 201)
    res2 = self.client().post('/api/v1/campaigns/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(self.campaign2))
    self.assertEqual(res2.status_code, 201)


    res_index = self.client().get('/api/v1/campaigns/',
                   headers={'Content-Type': 'application/json'})
    json_data = json.loads(res_index.data)
    self.assertEqual(len(json_data), 3)
    self.assertEqual(res_index.status_code, 200)

  def test_get_one_campaign(self):
    # create 2 campaigns
    res1 = self.client().post('/api/v1/campaigns/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(self.campaign1))
    self.assertEqual(res1.status_code, 201)
    campaign1_id = json.loads(res1.data)["id"]

    res2 = self.client().post('/api/v1/campaigns/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(self.campaign2))
    self.assertEqual(res2.status_code, 201)
  # GETTING A `308 Redirect` error. not sure why. works correctly on postman
    res_show = self.client().get('/api/v1/campaigns/{}'.format(campaign1_id),
                                 headers={'Content-Type': 'application/json'})
    self.assertEqual(res_show.status_code, 200)
    json_data = json.loads(res_show.data)
    self.assertEqual(self.campaign1["name"], json_data["name"])
    self.assertNotEqual(self.campaign2["name"], json_data["name"])
    self.assertEqual(self.campaign1["description"], json_data["description"])
    self.assertNotEqual(self.campaign2["description"], json_data["description"])
    self.assertEqual(self.campaign1["manager"], json_data["manager"])
    self.assertNotEqual(self.campaign2["manager"], json_data["manager"])
    self.assertEqual(self.campaign1["address"], json_data["address"])
    self.assertEqual(self.campaign1["min_contribution"], json_data["min_contribution"])
    self.assertNotEqual(self.campaign2["min_contribution"], json_data["min_contribution"])

  def test_campaigns_by_manager(self):
    # create 2 campaigns
    res1 = self.client().post('/api/v1/campaigns/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(self.campaign1))
    self.assertEqual(res1.status_code, 201)
    res2 = self.client().post('/api/v1/campaigns/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(self.campaign2))
    self.assertEqual(res2.status_code, 201)


    res_index = self.client().get('/api/v1/campaigns/manager/13',
                   headers={'Content-Type': 'application/json'},
                   )

    self.assertEqual(res_index.status_code, 200)
    json_data = json.loads(res_index.data)

    self.assertEqual(len(json_data), 1)
    self.assertEqual(self.campaign2["name"], json_data[0]["name"])
    self.assertEqual(self.campaign2["description"], json_data[0]["description"])
    self.assertEqual(self.campaign2["image"], json_data[0]["image"])
    self.assertEqual(self.campaign2["contributors"], json_data[0]["contributors"])
    self.assertEqual(self.campaign2["upvote"], json_data[0]["upvote"])
    self.assertEqual(self.campaign2["manager"], json_data[0]["manager"])
    self.assertEqual(self.campaign2["address"], json_data[0]["address"])
    self.assertEqual(self.campaign2["min_contribution"], json_data[0]["min_contribution"])

    #sad path test
    res_index = self.client().get('/api/v1/campaigns/manager/k',
                   headers={'Content-Type': 'application/json'},
                   )
    self.assertEqual(res_index.status_code, 404)
    json_data = json.loads(res_index.data)
    self.assertEqual("The entered manager has no campaigns", json_data["error"])
