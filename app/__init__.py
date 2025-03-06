from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_mail import Mail
from flask_migrate import Migrate

# Initialize Flask extensions
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"  # Redirect to login page if not logged in
socketio = SocketIO()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Load configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'password'

    # Initialize Flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)
    mail.init_app(app)

    # Flask-Migrate for handling migrations
    from flask_migrate import Migrate
    Migrate(app, db)

    # Import models here to avoid circular import
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register Blueprints
    from app.routes import routes
    from app.auth import auth
    app.register_blueprint(routes)
    app.register_blueprint(auth)

    # Ensure models are created
    with app.app_context():
        db.create_all()
        # Check if tables exist
        inspector = db.inspect(db.engine)
        if not inspector.get_table_names():
            print("No tables found in the database!")
        else:
            print(f"Tables found: {inspector.get_table_names()}")

    return app