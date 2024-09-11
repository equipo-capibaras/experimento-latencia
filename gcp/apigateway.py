import base64
import json
from flask import request, g

def _api_gateway_before_request():
    userinfo = request.headers.get('X-Apigateway-Api-Userinfo')

    if not userinfo:
        return

    userinfo = userinfo + '=' * (4 - len(userinfo) % 4)
    userinfo_decoded = base64.urlsafe_b64decode(userinfo)
    g.user_token = json.loads(userinfo_decoded)

def setup_apigateway(app):
    app.before_request(_api_gateway_before_request)
