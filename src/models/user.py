from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    password_hash = db.Column(db.String(102), nullable=True)
    api_key = db.Column(db.String(46), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
