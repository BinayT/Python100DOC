# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# cursor.execute("INSERT INTO books VALUES(2, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-sqlalchemy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


# Adding to the SQLite
# book_detail = Book(title="India Yatra", author="Binay Timilsina", rating='9.6')
# db.session.add(book_detail)
# db.session.commit()

# Reading from SQLite
# all_books = Book.query.all()
# for book in all_books:
#     print(book.title)

# Reading a specific book from SQLite
# book = Book.query.get(1)
# print(book)

# Updating a specific book's detail from SQLite
# book_to_update = Book.query.filter_by(title='Yo Mama').first()
# book_to_update.rating = 5.0
# db.session.commit()
# print(book_to_update)

# Updating a specific record with Primary key SQLite
# book_to_update_with_p_key = Book.query.get(3)
# book_to_update_with_p_key.title = 'Life in spain'
# db.session.commit()

# Deleting a specific book
# book_to_delete = Book.query.get(6)
# db.session.delete(book_to_delete)
# db.session.commit()