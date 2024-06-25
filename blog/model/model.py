from extensions import db, STATIC_FOLDER

import os
import uuid
from werkzeug.utils import secure_filename


upload_folder = os.path.join(STATIC_FOLDER, 'uploads')
os.makedirs(upload_folder, exist_ok=True)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(256), nullable=True)
    titre = db.Column(db.String(80), nullable=False)
    detail = db.Column(db.String(80), nullable=False)




    def __init__(self, titre, detail):

        self.titre = titre
        self.detail = detail

    def save_File(self, file):
        filename_str_uuid_uuid_ = str(uuid.uuid4()) + str(file.filename)
        filename = secure_filename(filename_str_uuid_uuid_)
        file.save(os.path.join(upload_folder, filename))

        self.image  = filename
