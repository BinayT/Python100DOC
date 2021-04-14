from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)
blogs = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
date_today = datetime.now().strftime("%m/%d/%Y")


@app.route("/")
def home_page():
    return render_template('index.html', blogs=blogs)


@app.route("/about")
def about_page():
    return render_template('about.html')


@app.route("/contact")
def contact_page():
    return render_template('contact.html')


@app.route('/post/<post_id>')
def post_page(post_id):
    blog_data = [data for data in blogs if data['id'] == int(post_id)]
    print(blog_data)
    return render_template('post.html', blog_data=blog_data, date=date_today)


if __name__ == '__main__':
    app.run(debug=True)