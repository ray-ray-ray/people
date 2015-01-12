"""
Data model for user roles.
"""
__author__ = 'RAY'

import datetime
import flask.ext.security
import people
db = people.db


class Role(db.Model, flask.ext.security.RoleMixin):
    """
    SQLAlchemy Object for Roles
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    time_created = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.now,
        nullable=False)
    time_modified = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
        nullable=False)
    time_removed = db.Column(db.DateTime(timezone=True))
    __table_args__ = (db.UniqueConstraint('name'),)

    def __init__(
            self,
            name,
            description,
            time_created=None,
            time_modified=None,
            time_removed=None):
        """
        Create a role object

        :param name: name of the role
        :param description: short description of the role
        :param time_created: datetime.datetime
        :param time_modified: datetime.datetime
        :param time_removed: datetime.datetime
        :return: None
        """
        self.name = name
        self.description = description
        if time_created is not None:
            self.time_created = time_created
        if time_modified is not None:
            self.time_modified = time_modified
        if time_removed is not None:
            self.time_removed = time_removed

    def __repr__(self):
        """
        String representation

        :return: <Role admin>
        """
        return '<Role %s>' % self.name