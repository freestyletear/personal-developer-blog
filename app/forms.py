from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Enter Your Desired Username Here...', validators=[
                           DataRequired(), Length(min=2, max=20)])
    email = StringField('Enter Your Valid Email Address Here...',
                        validators=[DataRequired(), Email()])
    password = PasswordField(
        'Enter Your Desired But Memorable Password Here...', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password Here...', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already in use')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email taken')


class LoginForm(FlaskForm):
    email = StringField('Enter Registered Email Here..',
                        validators=[DataRequired(), Email()])
    password = PasswordField(
        'Enter Registered Password Here...', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
