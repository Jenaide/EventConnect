from flask import (Flask, jsonify, render_template, request,
                   Response, flash, redirect, url_for, abort)
from models import *
from datetime import datetime
import dateutil.parser
import babel
from dotenv import load_dotenv
import os
from forms import *
from flask_bcrypt import Bcrypt, check_password_hash


load_dotenv()

app = Flask(__name__)
# connects to your postgresql database
app.config['SECRET_KEY'] = 'MindYoUrOWnBuSiNeSS'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tamlin@localhost:5432/eventconnectdb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)
bcrypt = Bcrypt(app)
app.env = 'development'


def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
        format = "EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format, locale='en')


app.jinja_env.filters['datetime'] = format_datetime

# generates the home page
@app.route('/')
def index():
    return render_template('pages/home.html')

@app.route('/register', methods=['POST', 'GET'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        # Check if user already exists
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            # If the user exists, display an appropriate error message
            flash('Username already exists. Please choose a different username.', 'danger')
            return redirect('/register')

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # If the user does not exist, create a new user
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. You can now log in!', category='success')
        return redirect('/login')
    
    return render_template('pages/register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        username=form.username.data,
        password=form.password.data

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully.', category='success')
            else:
                flash('Invalid username or password', category='error')
        else:
            flash('Username or password incorrect', category='error')
        return redirect('/dashboard')
    
    return render_template('pages/login.html', form=form, boolean=True)


@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    events = Event.query.all()
    return render_template('pages/dashboard.html', events=events)

@app.route('/create_event', methods=["GET", "POST"])
def add_event():

    form = CreateEventForm()

    if form.validate_on_submit():
        new_event = Event(
            name=form.name.data,
            description=form.description.data,
            location=form.location.data,
            organiser=form.organiser.data,
            ticket_price=form.ticket_price.data,
            capacity=form.capacity.data,
            date=form.date.data,
        )
        db.session.add(new_event)
        db.session.commit()
            
    return render_template('pages/create_event.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)