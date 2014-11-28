"""
Unit tests for the Person service.
"""
__author__ = 'RAY'


import nose.tools
import service.person
import test.unit.flask_sqlalchemy


class TestPerson(test.unit.flask_sqlalchemy.FlaskSQLAlchemyTest):
    """
    Testcases for the interacting with service.person
    """
    def test_create_myself(self):
        """
        Ensure that creator_id is set correctly when creating yourself.

        :return: None
        """
        me = service.person.create_myself('RAY Test', 'ray@ray.com', 'ray')
        nose.tools.assert_not_equal(
            me.creator_id,
            service.person.DEFAULT_CREATOR)
        nose.tools.assert_equal(me.id, me.creator_id)

    def test_get_none(self):
        """
        Ensure that get a non-existent user returns None (Flask-Login
        requirement).

        :return: None
        """
        nose.tools.assert_is_none(service.person.get_person(0))