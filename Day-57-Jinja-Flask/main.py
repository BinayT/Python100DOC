from flask import Flask, render_template
import random
import requests
import datetime

app = Flask(__name__)


@app.route('/')
def say_hi():
    random_number = random.randint(0, 10)
    current_year = datetime.datetime.now().year
    data = {
        'number': random_number,
        'year': current_year
    }
    return render_template('index.html', data=data)


@app.route('/guess/<name>')
def guess_gender_age(name):
    age = requests.get(f'https://api.agify.io?name={name}').json()
    gender = requests.get(f'https://api.genderize.io?name={name}').json()
    data = {
        'age': age['age'],
        'gender': gender['gender'],
        'name': name.title()
    }
    return render_template('genderize.html', data=data)


@app.route('/blog')
def get_posts():
    blogs = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
    print(blogs)
    return render_template('blogposts.html', blogs=blogs)


if __name__ == '__main__':
    app.run(debug=True)