from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)  # Store hashed password
    role = db.Column(db.String(10), nullable=False, default="user")  # 'admin' or 'user'

    def __repr__(self):
        return f"<User {self.email}>"