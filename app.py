"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request
from models import db, connect_db, Cupcake


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)


@app.route("/api/cupcakes")
def show_cupcakes():
    """show all cupcakes"""
    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route("/api/cupcakes/<int:cupcake_id>")
def show_cupcake(cupcake_id):
    """show info about a single cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """ create cupcake and add to db"""

    cupcake = Cupcake(
        flavor=request.json["flavor"],
        size=request.json["size"],
        rating=request.json["rating"],
        image=request.json["image"],
    )

    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize()), 201)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def edit_cupcake(cupcake_id):
    """ Edit the current cupcake """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.update()
    serialized = cupcake.serialize()

    return(jsonify(cupcake=serialized), 200)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """ DELETE this cupcake """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    deleted = cupcake.delete()

    return (jsonify(deleted=deleted), 200)
