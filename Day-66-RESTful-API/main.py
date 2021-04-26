from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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


def cafe_details(cafe):
    cafe_to_dict = {column: str(getattr(cafe, column)) for column in cafe.__table__.c.keys()}
    return cafe_to_dict


def cafes_list():
    res = [cafe_details(cafe) for cafe in Cafe.query.all()]
    return res


all_cafes = cafes_list()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

# Reading a random record
@app.route("/random", methods=['GET'])
def random_cafe():
    cafe = random.choice(Cafe.query.all())
    return jsonify(cafe=cafe_details(cafe))


# Reading all record
@app.route("/all", methods=['GET'])
def get_all_cafes():
    return jsonify(all_cafes=all_cafes)


# Reading a record
@app.route("/search", methods=['GET'])
def get_a_cafe():
    cafe_loc = request.args.get('loc')
    for cafe in all_cafes:
        if cafe['location'].lower() == cafe_loc.lower():
            return jsonify(cafe=cafe)
    return jsonify(error={'Not Found': f"Sorry, we couldn't find a cafe on {cafe_loc}"})

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
