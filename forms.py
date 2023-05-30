from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MorseForm(FlaskForm):
    text = StringField('Original text', validators=[DataRequired()])
    submit = SubmitField('Translate')
