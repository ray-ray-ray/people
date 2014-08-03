"""
Test that interact with the DB should inherit from this class.

https://pythonhosted.org/Flask-Testing/
"""
__author__ = 'RAY'


import flask.ext.testing
import people


class FlaskSQLAlchemyTest(flask.ext.testing.TestCase):

    config = {
        'SQLALCHEMY_DATABASE_URI':
        'postgresql+psycopg2://localhost:5432/people_test',
        'TESTING': True}

    def create_app(self):
        people.create_app(self.config)
        return people.app

    def setUp(self):
        people.db.create_all()

    def tearDown(self):
        people.db.session.remove()
        people.db.drop_all()