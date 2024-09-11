import json
from functools import wraps
from flask import g, Response

def class_route(self, rule, **options):
    def decorator(cls):
        self.add_url_rule(rule, view_func=cls.as_view(cls.__name__), **options)
        return cls

    return decorator

def requires_token(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'user_token' in g:
            return Response(json.dumps({'message': 'Token is missing', 'code': 401}), status=401, mimetype='application/json')
        if not 'sub' in g.user_token:
            return Response(json.dumps({'message': 'sub is missing in token', 'code': 401}), status=401, mimetype='application/json')
        if not 'cid' in g.user_token:
            return Response(json.dumps({'message': 'cid is missing in token', 'code': 401}), status=401, mimetype='application/json')
        if not 'aud' in g.user_token:
            return Response(json.dumps({'message': 'aud is missing in token', 'code': 401}), status=401, mimetype='application/json')
        return f(*args, **kwargs)
    return decorated_function
