from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length


class EditRatingForm(FlaskForm):
    rating = FloatField('Your rating out of 10. e.g 7.5', [DataRequired('Float num is required.')])
    review = StringField('Your Review', [DataRequired(), Length(min=2, max=255, message="Min Length 2 - Max Length 255")])
    submit = SubmitField('Done')


class SearchMovie(FlaskForm):
    title = StringField("Movie's Title", [DataRequired('Float num is required.')])
    submit = SubmitField('Done')