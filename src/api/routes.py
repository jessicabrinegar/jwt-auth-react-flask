"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# Create flask app 
api = Blueprint('api', __name__)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route("/login", methods=["POST"])
def create_login():
    # email = request.json.get("email", None)
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    # if email != "test" or password != "test":
    #     return jsonify({"message": "Bad username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


# @api.route("/register", methods=["POST"])
# def create_user():
#     request_body = request.get_json()
#     new_user = User(
#         email = request_body["email"],
#         username = request_body["username"],
#         password = request_body["password"],
#         is_active = True,
#     )
#     db.session.add(new_user)
#     db.session.commit()
#     access_token = create_access_token(identity=new_user.username)
#     return jsonify(access_token = access_token), 200
    # email = request.json.get("email", None)
    # username = request.json.get("username", None)
    # password = request.json.get("password", None)

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


@api.route("/hello", methods=["GET"])
# this means you are required to have the token to access the API
# test on postman using the authorizations: Bearer <token>
@jwt_required()
def get_hello():
    # ensure you know who is requesting
    username = get_jwt_identity()
    dict = {"message": "Hello, world! " + username}
    return jsonify(dict)


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