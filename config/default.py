"""
Flask and SQLAlchemy configs for app and db setup.
"""
__author__ = 'RAY'


class Config(object):
    """
    Default settings
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'


class DevelopmentConfig(Config):
    """
    Local dev
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://localhost:5432/people'
    SECRET_KEY = 'RAYismakingpeople'


class TestConfig(Config):
    """
    Unit tests
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://localhost:5432/people_test'
