import os


class Config(object):
    DEBUG = False
    SECRET_KEY = 'dev'
    PLATZI_DB_URI = os.environ['PLATZI_DB_URI']


class DevelopmentConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
