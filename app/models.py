from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from app import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Relationship: One user can book one seat at a time
    booking = db.relationship('Seat', backref='user', uselist=False)

class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seat_number = db.Column(db.String(10), unique=True, nullable=False)
    floor = db.Column(db.String(50), nullable=True)
    is_booked = db.Column(db.Boolean, default=False)
    booked_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)

    def book(self, user_id, duration_hours):
        """Book the seat for a user."""
        self.is_booked = True
        self.booked_by = user_id
        self.start_time = datetime.utcnow()
        self.end_time = self.start_time + timedelta(hours=duration_hours)

    def cancel_booking(self):
        """Cancel the seat booking."""
        self.is_booked = False
        self.booked_by = None
        self.start_time = None
        self.end_time = None