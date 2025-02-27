from flask import Blueprint

booking = Blueprint('booking', __name__)

@booking.route('/book')
def book():
    return "Booking page"
