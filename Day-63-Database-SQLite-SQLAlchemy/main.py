from flask import Flask, render_template, request, redirect, url_for
from form_class import BookEntryForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tryingsqllitetoday'
Bootstrap(app)

all_books = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/add", methods=['POST', 'GET'])
def add():
    form = BookEntryForm()
    if request.method == 'POST' and form.validate():
        name = form.book_name.data
        author = form.book_author.data
        rating = form.book_rating.data
        all_books.append({
            'name': name, 'author': author, 'rating': rating
        })
        print(all_books)
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

