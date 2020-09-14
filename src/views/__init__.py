from flask import Response, json
from ..models.ApiKey import ApiKey

def custom_response(res, status_code):
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )


def api_key_check(req):
  if 'api-key' not in req.headers:
    return custom_response({"error": "include an 'api-key' in request header"}, 400)
  elif not ApiKey.get_by_key(req.headers["api-key"]):
    return custom_response({"error": "incorrect API key"}, 400)
