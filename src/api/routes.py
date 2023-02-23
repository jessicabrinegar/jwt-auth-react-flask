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

# Allow CORS for all domains
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route("/login", methods=["POST"])
def create_token():
    # email = request.json.get("email", None)
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    # if email != "test" or password != "test":
    #     return jsonify({"message": "Bad username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@api.route("/register", methods=["POST"])
# @api.after_request()
def create_user():
    # body = request.get_json()
    name = request.json.get("name", None)
    username = request.json.get("username", None)
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    new_user = User(
        name = name,
        username = username,
        email = email,
        password = password,
        is_active = True,
    )
    # new_user = User(
    #     name = body["name"],
    #     email = body["email"],
    #     username = body["username"],
    #     password = body["password"],
    #     is_active = True,
    # )
    db.session.add(new_user)
    db.session.commit()
    return f"User {rb['name']} was created.", 200


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