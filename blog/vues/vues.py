from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from Account.controller.UserController import UserController
from blog.controller.controller import Controller


blog = Blueprint('blog', __name__)

article_controller = Controller()


@blog.route('article', methods=['POST'])
def article():
   # image = request.files['image']
  #  if not image:
#return jsonify({"msg": "Aucun Image Trouve dans la requete"}), 400
   # print(f"controller{image}")
    image = ""
    titre = request.json.get('titre', None)
    print(titre)
    detail = request.json.get('detail', None)
    print(detail)
    return article_controller.Article(image, titre, detail)


@blog.route('article', methods=['GET'])
def read():
    return article_controller.get_article()


@blog.route('article/<int:id>', methods=['DELETE'])
def dele(id):
    return article_controller.delete(id)
