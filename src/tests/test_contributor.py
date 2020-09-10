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

    self.campaign1 = {
        "name": "Test Campaign",
        "description": "test campaign description",
        "image": "test.jpg",
        "upvote": 2,
        "manager": "XYZ",
        "address": "X73K",
        "min_contribution": 5.0
    }

    with self.app.app_context():
      # create all db objects
      db.drop_all()
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

  def test_get_campaigns(self):
    create_contributor = self.client().post('/api/v1/contributor/',
                              headers={'Content-Type': 'application/json'},
                              data=json.dumps(self.contributor1))
    self.assertEqual(create_contributor.status_code, 201)

    create_campaign = self.client().post('/api/v1/campaigns/',
                              headers={'Content-Type': 'application/json'},
                              data=json.dumps(self.campaign1))
    self.assertEqual(create_campaign.status_code, 201)

    add_contributor_to_campaign = self.client().post('/api/v1/campaigns/X73K/contributor/XyZpekdA',
                              headers={'Content-Type': 'application/json'},
                               )
    self.assertEqual(add_contributor_to_campaign.status_code, 201)

    get_campaigns = self.client().get('/api/v1/contributor/XyZpekdA/campaigns',
                              headers={'Content-Type': 'application/json'},
                               )

    self.assertEqual(get_campaigns.status_code, 200)
    json_response = json.loads(get_campaigns.data)
    self.assertEqual('Test Campaign', json_response[0]['name'])
    self.assertEqual('test campaign description', json_response[0]['description'])
    self.assertEqual('test.jpg', json_response[0]['image'])
    self.assertEqual(2, json_response[0]['upvote'])
    self.assertEqual('XYZ', json_response[0]['manager'])
    self.assertEqual('X73K', json_response[0]['address'])
    self.assertEqual(5.0, json_response[0]['min_contribution'])
