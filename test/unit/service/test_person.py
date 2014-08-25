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
        me = service.person.create_myself('RAY Test')
        nose.tools.assert_not_equal(
            me.creator_id,
            service.person.DEFAULT_CREATOR)
        nose.tools.assert_equal(me.id, me.creator_id)