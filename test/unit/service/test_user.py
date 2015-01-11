"""
Unit tests for the User service.
"""
__author__ = 'RAY'


import nose.tools
import service.user
import test.unit.flask_sqlalchemy


class TestPerson(test.unit.flask_sqlalchemy.FlaskSQLAlchemyTest):
    """
    Testcases for the interacting with service.person
    """

    def test_get_none(self):
        """
        Ensure that get a non-existent user returns None (Flask-Login
        requirement).

        :return: None
        """
        nose.tools.assert_is_none(service.user.get_user(0))