import json
from flask import Blueprint, Response
from flask.views import MethodView
from .util import class_route

blp = Blueprint("Health Check", __name__)

@class_route(blp, "/v1/health/invoice")
class HealthCheck(MethodView):
    init_every_request = False

    def get(self):
        return Response(json.dumps({'status': 'Ok'}), status=200, mimetype='application/json')
