from flask import jsonify

from blog.model.model import Article
from extensions import db


class Controller:
    def __init__(self):
        self.model = Article

    def Article(self, image, titre, detail):
    #    print(f"controller{image}")
        Article = self.model(titre=titre, detail=detail)
       # Article.save_File(image)
        db.session.add(Article)

        db.session.commit()

        return jsonify(
            {"msg": " successfully"}), 201


    def get_article(self):
        article = self.model.query.all()

        return jsonify({
            "image": article.image,
            "titre": article.titre,
            "detail": article.detail
        }), 200


    def delete(self, id):
        article = self.model.query.filter_by(id=id).first()
        db.session.delete(article)
        db.session.commit()
        return jsonify(
            {"msg": "good"}), 201
