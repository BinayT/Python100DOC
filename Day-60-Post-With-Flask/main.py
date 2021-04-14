from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


def valid_login(name, password):
    if name != '' and password != '':
        return True
    else:
        return False


@app.route("/login", methods=["POST", "GET"])
def login():
    if valid_login(request.form["name"], request.form["password"]):
        data = {
            "name": request.form["name"],
            "password": request.form["password"]
        }
        return render_template('login.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
