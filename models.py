"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):

    __tablename__= "cupcakes"

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor=db.Column(db.String(30), nullable=False)
    size=db.Column(db.String(30), nullable=False)
    rating=db.Column(db.Float, nullable=False)
    image=db.Column(db.Text, default="https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg", nullable=False)

