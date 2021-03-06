from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    first_name = StringField('First name: ', validators=[DataRequired()])
    last_name = StringField('Last name: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired(), Length(min=6, message= "Passwords must be 6 characters or more!")])
    submit = SubmitField('Sign Up ')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
    submit = SubmitField('Sign In')

class AddressForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired('Please enter an address.')])
    submit = SubmitField("Search")
    