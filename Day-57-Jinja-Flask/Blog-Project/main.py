from flask import Flask, render_template
import requests
blogs = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()

app = Flask(__name__)


@app.route('/')
def home():
    data = [{'title': blog['title'], 'subtitle': blog['subtitle'], 'id': blog['id']} for blog in blogs]
    return render_template("index.html", blogs=data)


@app.route('/blog/<blog_id>')
def get_blog(blog_id):
    data = [blog for blog in blogs if int(blog_id) == blog['id']]
    print(data)
    return render_template('post.html', blog_details=data)


if __name__ == "__main__":
    app.run(debug=True)
