from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_mail import Mail
from flask_migrate import Migrate

# Initialize Flask extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
socketio = SocketIO()
mail = Mail()

def create_app():
    """Creates and configures the Flask application."""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    socketio.init_app(app)
    mail.init_app(app)

    login_manager.login_view = "auth.login"  # Redirect unauthorized users to login

    # Import and register Blueprints
    from .routes import routes
    from .auth import auth
    from .booking import booking

    app.register_blueprint(routes)
    app.register_blueprint(auth)
    app.register_blueprint(booking)

    # Ensure tables are created
    with app.app_context():
        db.create_all()

    return app

# Create the Flask app instance
app = create_app()
