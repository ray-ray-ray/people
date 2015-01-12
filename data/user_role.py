"""
Data model for UserRole mapping users to roles
"""
__author__ = 'RAY'

import datetime
import people
db = people.db


class UserRole(db.Model):
    """
    SQLAlchemy Object for UserRole rows
    """
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rid = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
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
    __table_args__ = (db.UniqueConstraint('uid', 'rid'),)

    def __init__(
            self,
            uid,
            rid,
            time_created=None,
            time_modified=None,
            time_removed=None):
        """
        Create a UserRole object

        :param uid: User.id
        :param rid: Role.id
        :param time_created: datetime.datetime
        :param time_modified: datetime.datetime
        :param time_removed: datetime.datetime
        :return: None
        """
        self.uid = uid
        self.rid = rid
        if time_created is not None:
            self.time_created = time_created
        if time_modified is not None:
            self.time_modified = time_modified
        if time_removed is not None:
            self.time_removed = time_removed