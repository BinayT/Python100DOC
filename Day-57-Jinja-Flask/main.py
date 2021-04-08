from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def say_hi():
    random_number = random.randint(0, 10)
    return render_template('index.html', random_number=random_number)


if __name__ == '__main__':
    app.run(debug=True)