from flask import Flask, render_template, request, redirect, url_for
from form_class import BookEntryForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tryingsqllitetoday'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


# Query to save book
def save_book(book):
    book_to_save = Book(title=book['title'], author=book['author'], rating=book['rating'])
    db.session.add(book_to_save)
    db.session.commit()


# Get all books in our DB along with their details
def get_all_books():
    return Book.query.all()


# Get specific book
def get_a_book(book_id):
    return Book.query.get(book_id)


# Updating book details:
def update_book(book_id, data):
    book_to_update = Book.query.get(book_id)

    book_to_update.title = data['title']
    book_to_update.author = data['author']
    book_to_update.rating = data['rating']
    print(book_to_update)
    db.session.commit()


# Delete a book
def delete_a_book(book_id):
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()


@app.route('/')
def home():
    return render_template('index.html', books=get_all_books())


@app.route("/add", methods=['POST', 'GET'])
def add():
    form = BookEntryForm()
    if request.method == 'POST' and form.validate():
        title = form.book_name.data
        author = form.book_author.data
        rating = form.book_rating.data

        books_to_save = {
            'title': title, 'author': author, 'rating': rating
        }
        save_book(books_to_save)

        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/edit', methods=['GET', 'POST'])
def edit_book_route():
    book_id = request.args.get('id')
    book_details = get_a_book(book_id)
    if request.method == 'POST':
        edit_book_title = request.form['title']
        edit_book_author = request.form['author']
        edit_book_rating = request.form['rating']
        edit_book_details = {
            'title': edit_book_title, 'author': edit_book_author, 'rating': edit_book_rating
        }
        update_book(book_id, edit_book_details)
        return redirect(url_for('home'))

    return render_template('edit_page.html', book=book_details)


@app.route('/delete')
def delete_book():
    book_to_delete = request.args.get('id')
    delete_a_book(book_to_delete)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

