from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from Account.controller.UserController import UserController

auth_api = Blueprint('auth_api', __name__)

user_controller = UserController()


@auth_api.route('login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    #return print(username, password)
    return user_controller.login(username, password)


@auth_api.route('register', methods=['POST'])
def register():
    nom = request.json.get('nom', None)
    prenom = request.json.get('prenom', None)
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not nom or not prenom or not username or not password:
        return {"msg": "Missing required fields"}, 400
    return user_controller.register(nom, prenom, username, password)


@auth_api.route('user', methods=['GET'])
@jwt_required()
def get_user():
    return user_controller.get_user()
