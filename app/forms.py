from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, validators, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])


class SignupForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    email = StringField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])
    confirm = PasswordField('Confirm Password', [DataRequired(), EqualTo('password', message='Passwords must match')])


class ContactForm(FlaskForm):
    fullname = StringField('Full Name*', [DataRequired()])
    email = EmailField('Email*', [DataRequired(), Email()])
    message = TextAreaField('Message*', [DataRequired()], render_kw={"rows": 10, "cols": 11})

