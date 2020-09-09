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
      db.drop_all()
      db.create_all()

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
    self.assertEqual(request["description"], json_data["description"])
    self.assertEqual(request["image"], json_data["image"])
    self.assertEqual(request["value"], json_data["value"])
    self.assertEqual(request["recipient"], json_data["recipient"])
    self.assertEqual(request["approvals"], json_data["approvals"])
