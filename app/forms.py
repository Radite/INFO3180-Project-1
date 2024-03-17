from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired, NumberRange

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=0)])
    type = SelectField('Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    bedrooms = IntegerField('# of Bedrooms', validators=[DataRequired(), NumberRange(min=0)])
    bathrooms = IntegerField('# of Bathrooms', validators=[DataRequired(), NumberRange(min=0)])
    photos = FileField('Photos', validators=[DataRequired()])
