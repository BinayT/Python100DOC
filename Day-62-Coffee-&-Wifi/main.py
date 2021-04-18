from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Length
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired("Cafeteria's Name is Required")])
    cafe_location = StringField('Cafe Location on Google Maps (URL)',
                                validators=[URL(), DataRequired('URL is required. Ex: https://goo.gl/maps/xxxxxxxxxxx)')])
    opening_time = StringField('Opening time (ex: 8AM)', validators=[DataRequired('Please indicate the opening time.'),
                                                                     Length(max=7)])
    closing_time = StringField('Closing time (ex: 11PM)', validators=[DataRequired('Please indicate the closing time.'),
                                                                      Length(max=7)])
    coffee_rating = SelectField('Coffee Rating', choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
                                validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength Rating', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                              validators=[DataRequired()])
    power_rating = SelectField('Power Socket Rating', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_details = [form.cafe.data, form.cafe_location.data, form.opening_time.data, form.closing_time.data,
                        form.coffee_rating.data, form.wifi_rating.data, form.power_rating.data]
        with open('cafe-data.csv', 'a', newline='', encoding="utf8") as csv_file:
            writer_object = csv.writer(csv_file)
            writer_object.writerow(cafe_details)
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows[0])
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
