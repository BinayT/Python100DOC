from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def cafe_details(cafe):
    cafe_to_dict = {column: str(getattr(cafe, column)) for column in cafe.__table__.c.keys()}
    return cafe_to_dict


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def random_cafe():
    cafe = random.choice(Cafe.query.all())
    return jsonify(cafe=cafe_details(cafe))
    # return jsonify(cafe={
    #     'name': cafe.name,
    #     'can_take_calls': cafe.can_take_calls,
    #     'coffee_price': cafe.coffee_price,
    #     'has_sockets': cafe.has_sockets,
    #     'has_toilet': cafe.has_toilet,
    #     'has_wifi': cafe.has_wifi,
    #     'img_url': cafe.img_url,
    #     'location': cafe.location,
    #     'map_url': cafe.map_url,
    #     'seats': cafe.seats,
    # })

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
