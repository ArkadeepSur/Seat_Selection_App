import os

class Config:
    SECRET_KEY = 'password'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Change to PostgreSQL later if needed
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
#    MAIL_USERNAME = os.getenv('EMAIL_USER')  # Set this in your environment variables
#    MAIL_PASSWORD = os.getenv('EMAIL_PASS')  # Set this in your environment variables
