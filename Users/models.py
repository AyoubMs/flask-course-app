from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def toDict(self):
        return dict(id=self.id, email=self.email, password=self.password, name=self.name)