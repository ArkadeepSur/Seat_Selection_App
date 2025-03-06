from flask import Blueprint, render_template
from flask_login import login_required

routes = Blueprint('routes', __name__)

@routes.route('/')
@login_required
def home():
    return render_template('home.html')  # Ensure home.html exists

@routes.route('/seat-selection')
@login_required
def seat_selection():
    return render_template('seat_selection.html')  # Ensure this template exists
