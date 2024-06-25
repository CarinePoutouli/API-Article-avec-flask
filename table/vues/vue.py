from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from Account.controller.UserController import UserController
from table.controller.controller import Controller

table = Blueprint('table', __name__)

produit_controller = Controller()


@table.route('produit', methods=['POST'])
def produit():
    nom = request.json.get('nom', None)
    quantite = request.json.get('quantite', None)
    prix_u = request.json.get('prix_u', None)
    prix_t = request.json.get('prix_t', None)

    return produit_controller.produit(nom, quantite, prix_u, prix_t)




@table.route('produit', methods=['GET'])
def read():
    return produit_controller.get_produit()



@table.route('produit/<int:id>', methods=['DELETE'])
def dele(id):

    return produit_controller.delete(id)





