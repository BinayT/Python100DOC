from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
Bootstrap(app)

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(255), nullable=False)
    img_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Movie %r>' % self.title


class RegistrationForm(FlaskForm):
    rating = StringField('Your rating out of 10. e.g 7.5', [DataRequired()])
    review = StringField('Your Review', [DataRequired()])
    submit = SubmitField('Done')


# Getting all movies
def get_all_movies():
    return Movie.query.all()


# Getting a movie
def get_a_movie(movie_id):
    return Movie.query.get(movie_id)


# Edit a movie
def edit_a_movie(movie_id, data):
    movie_to_edit = Movie.query.get(movie_id)
    movie_to_edit.rating = data['rating']
    movie_to_edit.review = data['review']
    db.session.commit()


# Deleting a movie
def delete_a_movie(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()


@app.route("/")
def home():
    return render_template("index.html", movies=get_all_movies())


# We must add (methods=['GET', 'POST']) on @app.route() to let us perform the HTTP task that we asked for.
@app.route("/edit", methods=['GET', 'POST'])
def edit_movie():
    movie_id = request.args.get('id')
    movie_to_update = get_a_movie(movie_id)
    form = RegistrationForm()

    if form.validate_on_submit() and request.method == 'POST':
        # This is how we get data from flask+bootstrap forms
        new_rating = form.rating.data
        new_review = form.review.data
        data_to_send = {
            'rating': new_rating,
            'review': new_review
        }

        edit_a_movie(movie_id, data_to_send)
        return redirect(url_for('home'))

    return render_template('edit.html', movie=movie_to_update, form=form)


@app.route('/delete')
def delete_movie():
    movie_id = request.args.get('id')
    delete_a_movie(movie_id)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
