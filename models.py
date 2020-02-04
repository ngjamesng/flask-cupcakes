"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy
from flask import request


db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    
    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String(30), nullable=False)
    size = db.Column(db.String(30), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    image = db.Column(
        db.Text, default="https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg", nullable=False)

    def serialize(self):
        """serialize a cupcake SQLAlchemy object to a python dictionary"""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image,
        }

    def delete(self):
        """ DELETE a cupcake """

        db.session.delete(self)
        db.session.commit()

        return "Deleted"

    def update(self):
        """ Updating this cupcake """

        self.flavor = request.json['flavor']
        self.size = request.json['size']
        self.rating = request.json['rating']
        self.image = request.json['image']

        db.session.add(self)
        db.session.commit()

        return self