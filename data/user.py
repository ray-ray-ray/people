"""
Data model for User
"""
__author__ = 'RAY'

import datetime
import people
db = people.db


class User(db.Model):
    """
    SQLAlchemy object for User
    """
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
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
    __table_args__ = (db.UniqueConstraint('email'), db.UniqueConstraint('pid'))

    def __init__(
            self,
            pid,
            email,
            password,
            time_created=None,
            time_modified=None,
            time_removed=None):
        """
        Create a user object.

        :param pid: data.person.id
        :param email: email address
        :param password: encrypted password
        :param time_created: datetime.datetime
        :param time_modified: datetime.datetime
        :param time_removed: datetime.datetime
        :return: None
        """
        self.pid = pid
        self.email = email
        self.password = password
        if time_created is not None:
            self.time_created = time_created
        if time_modified is not None:
            self.time_modified = time_modified
        if time_removed is not None:
            self.time_removed = time_removed

    def __repr__(self):
        """
        String representation

        :return: <User ray.allen.courtney@gmail.com>
        """
        return '<User %s>' % self.email