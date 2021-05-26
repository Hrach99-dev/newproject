from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FieldList, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileAllowed, FileField
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class LoginForm(FlaskForm, UserMixin):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm, UserMixin):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png'], 'The file format should be .jpg or .png.')], default='user.png')
    submit = SubmitField('Register')
