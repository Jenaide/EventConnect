from flask_wtf import FlaskForm as Form
from wtforms import (StringField, DateField, IntegerField, 
                     TextAreaField, PasswordField, SubmitField, 
                     EmailField, validators)
from wtforms.validators import (DataRequired, InputRequired, 
                                InputRequired, Email, EqualTo)

class CreateEventForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    description = TextAreaField(
        'description', validators=[DataRequired()]
    )
    location = StringField(
        'location', validators=[DataRequired()]
    )
    organiser = StringField(
        'organiser', validators=[DataRequired()]
    )
    ticket_price = IntegerField(
        'ticket_price', validators=[DataRequired()]
    )
    capacity = IntegerField(
        'capacity', validators=[DataRequired()]
    )
    date = DateField(
        'date', 
        validators=[DataRequired()]
    )


# Login Form
class LoginForm(Form):
    username = StringField(
        'Username', validators=[InputRequired()]
    )
    email = EmailField(
        'Email', validators=[InputRequired()]
    )
    password = PasswordField(
        'Password', validators=[InputRequired()]
    )
    submit = SubmitField('Log In')


# Registration Form
class RegistrationForm(Form):
    username = StringField(
        'Username', validators=[InputRequired()]
    )
    email = EmailField(
        'Email', validators=[InputRequired(), Email()]
    )
    password = PasswordField(
        'Password', validators=[InputRequired(), validators.Length(min=8)]
    )
    confirm_password = PasswordField(
        'Confirm Password', validators=[InputRequired(), 
                                        EqualTo('password', 
                                                message='Passwords must match')])
    submit = SubmitField('Sign Up')