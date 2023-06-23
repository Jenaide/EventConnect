from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class Event(db.Model):
    __tablename__ = 'Event'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    discription = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    organizer = db.Column(db.Integer(), db.ForeignKey('User.id'), nullable=False)
    ticket_price = db.Column(db.Integer(), nullable=False)
    capacity = db.Column(db.Integer(), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Event {}>'.format(self.name)
    
class Booking(db.Model):
    __tablename__ = 'Booking'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer(), db.ForeignKey('event.id'), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    tickets = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return '<Booking {}>'.format(self.name)
