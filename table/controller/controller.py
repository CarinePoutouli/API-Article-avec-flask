from flask import jsonify

from table.model.model import Produit
from extensions import db
class Controller:
    def __init__(self):
        self.model = Produit

    def produit(self, nom, quantite, prix_u, prix_t):
            produit = self.model(nom=nom, quantite=quantite, prix_u=prix_u, prix_t=prix_t)
            produit.quantite= quantite
            db.session.add(produit)

            db.session.commit()

            return jsonify(
                {"msg": "User created successfully"}), 201

    def get_produit(self):

        produit = self.model.query.all()

        return jsonify({
            "nom": produit.nom,
            "quantite": produit.quantite,
            "prix_u": produit.prix_u,
            "prix_t": produit.prix_t
        }), 200

    def delete(self, id):
        produit = self.model.query.filter_by(id=id).first()
        db.session.delete(produit)
        db.session.commit()
        return jsonify(
                {"msg": "good"}), 201



