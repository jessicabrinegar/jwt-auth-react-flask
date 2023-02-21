"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


# registration route for a user -- send post request to create new instance of class User to save to database
# send back the JWT in response
# @api.route('/register', methods=['POST'])
# def create_user():
    # request body
    # rb = request.get_json()
    # new_user = User(
    #     email=rb["email"], 
        # need to hash the password!
        # password=bcrypt.hashpw(rb["password"].encode('utf-8'), bcrypt.gensalt()), 
        # is_active=True
        # )
    # db.session.add(new_user)
    # db.session.commit()
    # access_token = create_access_token(identity=new_user.email)
    # return access_token, 200

#@api.route('/restricted', methods=['GET'])
# to make a restricted route, apply the following decorator: 
#@jwt_required
# def get_restricted():