from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_ley=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
