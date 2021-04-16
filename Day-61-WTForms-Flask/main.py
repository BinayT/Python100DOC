from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisatopsecret?!?!'


class LoginForm(FlaskForm):
    email = StringField('Email : ', validators=[DataRequired()])
    password = PasswordField('Password : ', validators=[DataRequired()])


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)