# Needed setting secret key, email and psswd
from os import environ
class Config:
    SECRET_KEY = 'qwertyuiop'
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = environ.get('USER')
    MAIL_PASSWORD = environ.get('password')
