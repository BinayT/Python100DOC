from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os.path
from main import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


# With this we checking if the file already exists or not, if it doesn't exist then we create a new DB
if not os.path.isfile('books-list.db'):
    db.create_all()


# Query to save book
def save_book(book):
    book_to_save = Book(title=book['title'], author=book['author'], rating=book['rating'])
    db.session.add(book_to_save)
    db.session.commit()