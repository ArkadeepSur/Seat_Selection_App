from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return "Welcome to the Seat Selection App!"