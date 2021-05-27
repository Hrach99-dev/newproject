from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FieldList, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileAllowed, FileField
from wtforms import ValidationError
from flask_login import current_user
from myproject.modles import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()] )
    submit = SubmitField('Register')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered!')

    def check_phone(self,field):
        if User.query.filter_by(phone=field.data).first():
            raise ValidationError('Your phone has been registered!')


class UpdateUserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    picture = FileField('Profile Picture', validators=[FileAllowed(['png', 'jpg'])])
    submit = SubmitField('Update')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered!')

    def check_phone(self,field):
        if User.query.filter_by(phone=field.data).first():
            raise ValidationError('Your phone has been registered!')