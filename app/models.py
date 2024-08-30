from app.extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(256))

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f"<User {self.username}>"
