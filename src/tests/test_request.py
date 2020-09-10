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
      res = self.client().post('/api/v1/campaigns/',
                         headers={'Content-Type': 'application/json'},
                         data=json.dumps(self.campaign1))
      self.campaign1_id = json.loads(res.data)["id"]
      res = self.client().post('/api/v1/campaigns/',
                         headers={'Content-Type': 'application/json'},
                         data=json.dumps(self.campaign2))
      self.campaign2_id = json.loads(res.data)["id"]

  def test_campaign_creation_in_setup(self):
    res = self.client().get('/api/v1/campaigns/', headers={'Content-Type': 'application/json'})
    json_data = json.loads(res.data)
    self.assertEqual(len(json_data), 2)

  
  def test_request_creation(self):
    self.request1['campaign_id'] = self.campaign1_id
    res = self.client().post('/api/v1/requests/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.request1))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 201)

    self.assertEqual(self.request1["campaign_id"], json_data["campaign_id"])
    self.assertEqual(self.request1["description"], json_data["description"])
    self.assertEqual(self.request1["image"], json_data["image"])
    self.assertEqual(self.request1["value"], json_data["value"])
    self.assertEqual(self.request1["recipient"], json_data["recipient"])
    self.assertEqual(self.request1["approvals"], json_data["approvals"])
  
  def test_request_update(self):
    self.request1['campaign_id'] = self.campaign1_id
    res = self.client().post('/api/v1/requests/', headers={'Content-Type': 'application/json'}, data=json.dumps(self.request1))
    request1_id = json.loads(res.data)['id']

    request1_update = {
        'description': 'new description',
        'value': 999,
        'recipient': 'dog',
    }
    res = self.client().put(f'/api/v1/requests/{request1_id}',
                             headers={'Content-Type': 'application/json'}, data=json.dumps(request1_update))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)

    self.assertEqual(self.request1["campaign_id"], json_data["campaign_id"])
    self.assertNotEqual(self.request1["description"], json_data["description"])
    self.assertEqual(request1_update["description"], json_data["description"])
    self.assertEqual(self.request1["image"], json_data["image"])
    self.assertNotEqual(self.request1["value"], json_data["value"])
    self.assertEqual(request1_update["value"], json_data["value"])
    self.assertNotEqual(self.request1["recipient"], json_data["recipient"])
    self.assertEqual(request1_update["recipient"], json_data["recipient"])
    self.assertEqual(self.request1["approvals"], json_data["approvals"])

  def test_request_delete(self):
    self.request1['campaign_id'] = self.campaign1_id
    res = self.client().post('/api/v1/requests/',
                             headers={'Content-Type': 'application/json'}, data=json.dumps(self.request1))
    request1_id = json.loads(res.data)['id']

    self.request2['campaign_id'] = self.campaign1_id
    res = self.client().post('/api/v1/requests/',
                             headers={'Content-Type': 'application/json'}, data=json.dumps(self.request2))

    res_index = self.client().get(
        '/api/v1/requests/', headers={'Content-Type': 'application/json'})
    json_data = json.loads(res_index.data)

    self.assertEqual(len(json_data), 2)

    res_delete = self.client().delete('/api/v1/requests/{}'.format(request1_id),
                                      headers={'Content-Type': 'application/json'})
    self.assertEqual(res_delete.status_code, 200)

    res_index = self.client().get('/api/v1/requests/', headers={'Content-Type': 'application/json'})
    json_data = json.loads(res_index.data)
    self.assertEqual(len(json_data), 1)

  def test_one_request(self):
    self.request1['campaign_id'] = self.campaign1_id
    res1 = self.client().post('/api/v1/requests/',
                             headers={'Content-Type': 'application/json'}, data=json.dumps(self.request1))
    request1_id = json.loads(res1.data)['id']

    self.request2['campaign_id'] = self.campaign1_id
    res2 = self.client().post('/api/v1/requests/',
                             headers={'Content-Type': 'application/json'}, data=json.dumps(self.request2))
    request2_id = json.loads(res2.data)['id']

    res1_get = self.client().get('/api/v1/requests/{}'.format(request1_id), headers={'Content-Type': 'application/json'})
    json_data1 = json.loads(res1_get.data)

    res2_get = self.client().get('/api/v1/requests/{}'.format(request2_id), headers={'Content-Type': 'application/json'})
    json_data2 = json.loads(res2_get.data)

    self.assertEqual(self.request1["value"], json_data1["value"])
    self.assertNotEqual(self.request2["value"], json_data1["value"])
    
    self.assertEqual(self.request2["value"], json_data2["value"])
    self.assertNotEqual(self.request1["value"], json_data2["value"])

    self.assertEqual(self.request1["description"], json_data1["description"])
    self.assertNotEqual(self.request2["description"], json_data1["description"])

    self.assertEqual(self.request2["description"], json_data2["description"])
    self.assertNotEqual(self.request1["description"], json_data2["description"])

    





    

    # send a request
    # res = self.client().post('/api/v1/campaigns/',
    #                           headers={'Content-Type': 'application/json'},
    #                           data=json.dumps(self.campaign1))
    # self.assertEqual(res.status_code, 201)
    # campaign_id = json.loads(res.data)["id"]

    # request = {
    #     'campaign_id': campaign_id,
    #     'description': 'Buy supplies',
    #     'image': 'https://picsum.photos/200/300',
    #     'value': 100,
    #     'recipient': 'kfh7DFh38H',
    #     'approvals': 0,

    # }

    # res = self.client().post('/api/v1/requests/',
    #                           headers={'Content-Type': 'application/json'},
    #                           data=json.dumps(request))
    # self.assertEqual(res.status_code, 201)
    # json_data = json.loads(res.data)

    # self.assertEqual(request["campaign_id"], json_data["campaign_id"])
    # self.assertEqual(request["description"], json_data["description"])
    # self.assertEqual(request["image"], json_data["image"])
    # self.assertEqual(request["value"], json_data["value"])
    # self.assertEqual(request["recipient"], json_data["recipient"])
    # self.assertEqual(request["approvals"], json_data["approvals"])

  # def update_request(self):
  #   request1_update = {
  #       'campaign_id': 0,
  #       'description': 'Buy supplies',
  #       'image': 'https://picsum.photos/200/300',
  #       'value': 100,
  #       'recipient': 'kfh7DFh38H',
  #       'approvals': 0,
  #   }
