"""
Tests that interact with the DB should inherit from this class.

Make sure you set the FLASKCONFIG env variable to a testing configuration class.

https://pythonhosted.org/Flask-Testing/
"""
__author__ = 'RAY'


import flask.ext.testing
import people


class FlaskSQLAlchemyTest(flask.ext.testing.TestCase):
    """
    Base class for any test that interacts with the DB.

    app is the Flask app
    db is the SQLAlchemy object
    """
    app = None
    db = None

    def create_app(self):
        """
        Get the Flask app and SQLAlchemy object from the people app.

        :return: the Flask app
        """
        self.app = people.app
        self.db = people.db
        return self.app

    def setUp(self):
        """
        Create the schemas.

        :return: None
        """
        self.db.create_all()

    def tearDown(self):
        """
        Drop all the schemas.

        :return: None
        """
        self.db.session.remove()
        self.db.drop_all()