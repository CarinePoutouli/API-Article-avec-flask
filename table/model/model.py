from extensions import db


class Produit(db.Model):
    __tablename__ = 'produits'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    quantite = db.Column(db.Integer(), nullable=False)
    prix_u = db.Column(db.Float(), unique=True, nullable=False)
    prix_t = db.Column(db.Float(), unique=True, nullable=False)



    def __init__(self, nom, quantite, prix_u, prix_t):
        self.nom = nom
        self.quantite = quantite
        self.prix_u = prix_u
        self.prix_t = prix_t

