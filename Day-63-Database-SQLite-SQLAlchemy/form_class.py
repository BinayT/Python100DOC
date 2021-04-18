from wtforms import StringField, SelectField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class BookEntryForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired("Book's name is required.")])
    book_author = StringField('Book Author', validators=[DataRequired("Book's author name is required.")])
    book_rating = SelectField('Rating', choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    submit = SubmitField('Add Book', render_kw={'style': 'color: #000; background-color: #0dcaf0;'
                                                         ' border-color: #0dcaf0; margin-top:15px'})
