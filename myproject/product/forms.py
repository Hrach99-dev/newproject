from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileField
from wtforms import ValidationError


class ProductForm(FlaskForm):
    product_name = StringField('Product name', validators=[DataRequired()])
    product_info = StringField('Product info', validators=[DataRequired()])
    product_price = StringField('Product price', validators=[DataRequired()])
    submit = SubmitField('Add Product')