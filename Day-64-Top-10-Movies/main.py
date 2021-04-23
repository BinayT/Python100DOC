from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from forms import EditRatingForm, SearchMovie
from request_movie import MovieSearcher

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


# Getting all movies from DB
def get_all_movies():
    return Movie.query.all()


# Getting a movie from DB
def get_a_movie(movie_id):
    return Movie.query.get(movie_id)


# Edit a movie from DB
def edit_a_movie(movie_id, data):
    movie_to_edit = Movie.query.get(movie_id)
    movie_to_edit.rating = data['rating']
    movie_to_edit.review = data['review']
    db.session.commit()


# Deleting a movie from DB
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
    # This is how we get query string, in our case its /edit?id=X
    movie_id = request.args.get('id')
    movie_to_update = get_a_movie(movie_id)
    form = EditRatingForm()

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


# Since the /delete route don't have or need any template for movie deletion, we simply redirect to home.
@app.route('/delete')
def delete_movie():
    movie_id = request.args.get('id')
    delete_a_movie(movie_id)
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add_movie():
    form = SearchMovie()
    if form.validate_on_submit() and request.method == "POST":
        movie_name = form.title.data

        # We initialize our class here and on next line we pass the movie's name to the method, which searches movies.
        movies_class = MovieSearcher()
        movies = movies_class.get_all_movies(movie_name)

        # Here I'm redirecting the user to the select.html file along with the data of the movies.
        return render_template('select.html', movies=movies)

    return render_template('add.html', form=form)


@app.route("/select_movie", methods=['GET', 'POST'])
def select_movie():
    return render_template('select.html')


if __name__ == '__main__':
    app.run(debug=True)
