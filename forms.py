from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField


class RegistrationForm(FlaskForm):
    nickname = StringField('Nickname')
    email = StringField('Email')
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

