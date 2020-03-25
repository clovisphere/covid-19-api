from flask import jsonify, g
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from .models import User

auth = HTTPBasicAuth()
auth_token = HTTPTokenAuth()

@auth.verify_password
def verify_password(username, password):
    g.user = User.query.filter_by(username=username).first()
    if g.user is None:
        return False
    return g.user.verify_password(password)

@auth.error_handler
def unauthorized():
    response = jsonify({'status': 401, 'error': 'unauthorized', 'message': 'please authenticate'})
    response.status_code = 401
    return response

@auth_token.verify_token
def verify_auth_token(token):
    g.user = User.verify_auth_token(token)
    return g.user is not None

@auth_token.error_handler
def unauthorized_token():
    response = jsonify({'status': 401, 'error': 'unauthorized', 'message': 'please send your authentication token'})
    response.status_code = 401
    return response
