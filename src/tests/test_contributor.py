import pdb
import unittest
import os
import json
# import flask_sqlalchemy
from ..models.Contributor import Contributor
from ..models.Campaign import Campaign
from ..models.CampaignContributor import CampaignContributor
from ..app import create_app, db

class ContributorTest(unittest.TestCase):
  # set up the tests with 2 contributors
  # This runs before EVERY test. not once before all
  def setUp(self):
    self.app = create_app('testing')
    self.client = self.app.test_client
    self.contributor1 = {
        "address": "XyZpekdA",
        "email": "test@email.com"
    }
    self.contributor2 = {
        "address": "AaBbCc9"
    }

    with self.app.app_context():
      # create all db objects
      db.create_all()
      # delete test campaigns by name
      existing_contributor1 = Contributor.get_contributor_by_address(self.contributor1["address"])
      if existing_contributor1:
        existing_contributor1.delete()
      existing_contributor2 = Contributor.get_contributor_by_address(self.contributor2["address"])
      if existing_contributor2:
        existing_contributor2.delete()
#
  def test_contributor_creation(self):
    # send a request
    res = self.client().post('/api/v1/contributor/',
                              headers={'Content-Type': 'application/json'},
                              data=json.dumps(self.contributor1))
    self.assertEqual(res.status_code, 201)
    json_data = json.loads(res.data)
    self.assertEqual(self.contributor1["address"], json_data["address"])
    self.assertEqual(self.contributor1["email"], json_data["email"])

  def test_contributor_update(self):
    contributor2_update = {
      "email": 'update@email.com'
    }
    response = self.client().post('/api/v1/contributor/',
                             headers={'Content-Type': 'application/json'},
                             data=json.dumps(self.contributor2))
    self.assertEqual(response.status_code, 201)

    contributor2_id = json.loads(response.data)["id"]
    updated_response = self.client().put('/api/v1/contributor/{}'.format(contributor2_id),
                            headers={'Content-Type': 'application/json'},
                            data=json.dumps(contributor2_update))

    self.assertEqual(updated_response.status_code, 200)
    json_data = json.loads(updated_response.data)
    self.assertEqual("update@email.com", json_data["email"])
    self.assertNotEqual("test@email.com", json_data["email"])
#
#   def test_delete(self):
#     res = self.client().post('/api/v1/campaigns/',
#                               headers={'Content-Type': 'application/json'},
#                               data=json.dumps(self.campaign1))
#     self.assertEqual(res.status_code, 201)
#     campaign1_id = json.loads(res.data)["id"]
#
#     # delete campaign
#     res_delete = self.client().delete('/api/v1/campaigns/{}'.format(campaign1_id), headers={'Content-Type': 'application/json'})
#     self.assertEqual(res_delete.status_code, 200)
#
#   def test_get_all_campaigns(self):
#     # create 2 campaigns
#     res1 = self.client().post('/api/v1/campaigns/',
#                              headers={'Content-Type': 'application/json'},
#                              data=json.dumps(self.campaign1))
#     self.assertEqual(res1.status_code, 201)
#     res2 = self.client().post('/api/v1/campaigns/',
#                              headers={'Content-Type': 'application/json'},
#                              data=json.dumps(self.campaign2))
#     self.assertEqual(res2.status_code, 201)
#
#
#     res_index = self.client().get('/api/v1/campaigns/',
#                    headers={'Content-Type': 'application/json'})
#     json_data = json.loads(res_index.data)
#     self.assertEqual(len(json_data), 3)
#     self.assertEqual(res_index.status_code, 200)
#
#   def test_get_one_campaign(self):
#     # create 2 campaigns
#     res1 = self.client().post('/api/v1/campaigns/',
#                              headers={'Content-Type': 'application/json'},
#                              data=json.dumps(self.campaign1))
#     self.assertEqual(res1.status_code, 201)
#     campaign1_id = json.loads(res1.data)["id"]
#
#     res2 = self.client().post('/api/v1/campaigns/',
#                              headers={'Content-Type': 'application/json'},
#                              data=json.dumps(self.campaign2))
#     self.assertEqual(res2.status_code, 201)
#   # GETTING A `308 Redirect` error. not sure why. works correctly on postman
#     res_show = self.client().get('/api/v1/campaigns/{}'.format(campaign1_id),
#                                  headers={'Content-Type': 'application/json'})
#     self.assertEqual(res_show.status_code, 200)
#     json_data = json.loads(res_show.data)
#     self.assertEqual(self.campaign1["name"], json_data["name"])
#     self.assertNotEqual(self.campaign2["name"], json_data["name"])
#     self.assertEqual(self.campaign1["description"], json_data["description"])
#     self.assertNotEqual(self.campaign2["description"], json_data["description"])
#     self.assertEqual(self.campaign1["manager"], json_data["manager"])
#     self.assertNotEqual(self.campaign2["manager"], json_data["manager"])
#     self.assertEqual(self.campaign1["address"], json_data["address"])
#     self.assertEqual(self.campaign1["min_contribution"], json_data["min_contribution"])
#     self.assertNotEqual(self.campaign2["min_contribution"], json_data["min_contribution"])
#
#   def test_campaigns_by_manager(self):
#     # create 2 campaigns
#     res1 = self.client().post('/api/v1/campaigns/',
#                              headers={'Content-Type': 'application/json'},
#                              data=json.dumps(self.campaign1))
#     self.assertEqual(res1.status_code, 201)
#     res2 = self.client().post('/api/v1/campaigns/',
#                              headers={'Content-Type': 'application/json'},
#                              data=json.dumps(self.campaign2))
#     self.assertEqual(res2.status_code, 201)
#
#
#     res_index = self.client().get('/api/v1/campaigns/manager/13',
#                    headers={'Content-Type': 'application/json'},
#                    )
#
#     self.assertEqual(res_index.status_code, 200)
#     json_data = json.loads(res_index.data)
#
#     self.assertEqual(len(json_data), 1)
#     self.assertEqual(self.campaign2["name"], json_data[0]["name"])
#     self.assertEqual(self.campaign2["description"], json_data[0]["description"])
#     self.assertEqual(self.campaign2["image"], json_data[0]["image"])
#     self.assertEqual(self.campaign2["upvote"], json_data[0]["upvote"])
#     self.assertEqual(self.campaign2["manager"], json_data[0]["manager"])
#     self.assertEqual(self.campaign2["address"], json_data[0]["address"])
#     self.assertEqual(self.campaign2["min_contribution"], json_data[0]["min_contribution"])
#
#     #sad path test
#     res_index = self.client().get('/api/v1/campaigns/manager/k',
#                    headers={'Content-Type': 'application/json'},
#                    )
#     self.assertEqual(res_index.status_code, 404)
#     json_data = json.loads(res_index.data)
#     self.assertEqual("The entered manager has no campaigns", json_data["error"])
