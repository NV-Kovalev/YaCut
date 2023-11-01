import os


class Config(object):
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='SECRET_KEY')


BASE_URL = os.getenv('HOST', default='http://localhost/')
