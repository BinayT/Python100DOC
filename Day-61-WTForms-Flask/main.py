from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisatopsecret?!?!'
Bootstrap(app)


class LoginForm(FlaskForm):
    email = StringField('Email : ', validators=[DataRequired(), Email()])
    password = PasswordField('Password : ', validators=[DataRequired(), Length(min=8)])
    submit_label = SubmitField('Log In')


@app.route("/")
def home():
    return render_template('index.html')


def render_success():
    return render_template('success.html')


def render_denied():
    return render_template('denied.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = 'admin@email.com'
        password = '12345678'
        if form.email.data == email and form.password.data == password:
            return render_success()
        else:
            return render_denied()
    return render_template('login.html', form=form)


@app.route('/form')
def formm():
    form = LoginForm()
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)