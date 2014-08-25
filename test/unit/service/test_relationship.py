"""
Unit tests for the relationship service.
"""
__author__ = 'RAY'


import data.relationship
import nose.tools
import service.relationship
import test.unit.flask_sqlalchemy


class TestRelationship(test.unit.flask_sqlalchemy.FlaskSQLAlchemyTest):
    """
    Testcases for interacting with service.relationship
    """
    def test_create_relationship(self):
        """
        Ensure create_relationship enforces relationship type restrictions.

        :return: None
        """
        #
        # Numeric type
        #
        nose.tools.assert_raises(
            TypeError,
            service.relationship.create_relationship,
            (1, 1, 1))

        #
        # Mom is OK
        #
        relationship = service.relationship.create_relationship(
            data.relationship.Rtype.mom,
            1,
            1)
        nose.tools.assert_equal(
            relationship.type,
            data.relationship.Rtype.mom.value)