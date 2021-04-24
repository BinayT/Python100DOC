from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from forms import EditRatingForm, SearchMovie
from request_movie import MovieSearcher

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
Bootstrap(app)
POSTER_PATH = 'https://image.tmdb.org/t/p/original'

db = SQLAlchemy(app)

# We initialize the movie searching class here so we can use it's methods in throughout the app.
movies_class = MovieSearcher()


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(255), nullable=True)
    img_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Movie %r>' % self.title


# Getting all movies from DB
def get_all_movies():
    # Here we getting all the movies on descending order, depending upon their rating
    movie_on_desc_order = Movie.query.order_by(Movie.rating.desc()).all()
    ranking = 1

    # With this for loop each time we hit the home route, we giving new ranking to each movie, hence it keeps track
    # of the movie's ranking
    for movie in movie_on_desc_order:
        movie.ranking = ranking
        ranking += 1
    return movie_on_desc_order


# Getting a movie from DB with the DB's id.
def get_a_movie(movie_id):
    return Movie.query.get(movie_id)


# Edit a movie from DB alongside given DB id for the film and data provided from the form.
def edit_a_movie(movie_id, data):
    movie_to_edit = Movie.query.get(movie_id)
    movie_to_edit.rating = data['rating']
    movie_to_edit.review = data['review']
    db.session.commit()


# Deleting a movie from DB with the given DB id
def delete_a_movie(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()


# Here we sending all movies from the DB as arguments to later render them on the home page.
@app.route("/")
def home():
    return render_template("index.html", movies=get_all_movies())


# We must add (methods=['GET', 'POST']) on @app.route() to let us perform the HTTP task that we asked for.
@app.route("/edit", methods=['GET', 'POST'])
def edit_movie():
    # This is how we get query string, in our case its /edit?id=X
    movie_id = request.args.get('id')
    movie_to_update = get_a_movie(movie_id)

    # Here I'm initializing a bootstrap FlaskForm so later i can use validate_on_submit() method for auto validation.
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
        # After editing/giving our personal rating and review to the movie, we instantly redirect to the home page.
        return redirect(url_for('home'))

    # Here we are passing the movie object from the DB to know which movie we editing and flask form to
    # create quick forms with bootstrap. Check out edit.html to see how the movie object is implemented.
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

        # We initialize our class above and on this line we pass the movie's name to the method, which searches movies.
        movies = movies_class.get_all_movies(movie_name)

        # Here I'm redirecting the user to the select.html file along with movie object which contains all the movies
        # and their details. It's a list of movies.
        return render_template('select.html', movies=movies)

    return render_template('add.html', form=form)


@app.route("/select_movie")
def select_movie():
    # We get the movie's id from the movie database API, not the ID of our local database.
    movie_api_id = request.args.get("movie_id")
    if movie_api_id:
        # Once if there is the api's id, then we search for that movie with it's id and later save it to our database.
        movie = movies_class.get_a_movie(movie_api_id)
        movie_to_save = Movie(title=movie['original_title'], description=movie['overview'],
                              year=movie['release_date'][:4], img_url=f'{POSTER_PATH}/{movie["poster_path"]}')
        db.session.add(movie_to_save)
        db.session.commit()

        # Once we save the movie to our database, then we access the saved movie, by simply accessing the
        # "movie_to_save" object to get it's ID (the DB id now, not the id of the API)) and send it to the edit_movie
        # because now edit_movie needs the DB's id and not the API's id.
        return redirect(url_for('edit_movie', id=movie_to_save.id))


if __name__ == '__main__':
    app.run(debug=True)
