from flask import request, json, Response, Blueprint, jsonify
from marshmallow import ValidationError
from sqlalchemy import exc
from ..models.ApiKey import ApiKey, ApiKeySchema
from . import custom_response, api_key_check
import secrets


api_key_api = Blueprint('api_key_api', __name__)
api_key_schema = ApiKeySchema()


@api_key_api.route('/', methods=['POST'])
def create():
  try:
    new_key = secrets.token_urlsafe(10)
    req_data = request.get_json()
    req_data['key'] = new_key
    data = api_key_schema.load(req_data)
  except ValidationError as err:
    return custom_response(err.messages, 400)
  except:
    return custom_response({"error": "Please provide an email in request body"}, 400)

  api_key_info = ApiKey(data)
  api_key_info.save()

  api_key_data = api_key_schema.dump(api_key_info)
  return custom_response(api_key_data, 201)

@api_key_api.route('/', methods=['GET'])
def get_all_api_keys():
  if api_key_check(request):
    return api_key_check(request)
  else:
    api_key_data = []
    for key in ApiKey.get_all():
      api_key_data.append(api_key_schema.dump(key))
    return custom_response(api_key_data,200)



