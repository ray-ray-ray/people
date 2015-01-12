"""
Data model for Relationship
"""
__author__ = 'RAY'


import datetime
import enum
import people
db = people.db


@enum.unique
class Rtype(enum.Enum):
    """
    Allowable relationship types
    """
    mom = 1
    dad = 2


class Relationship(db.Model):
    """
    SQLAlchemy object for Relationship
    """
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer, nullable=False)
    from_pid = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    to_pid = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
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
    __table_args__ = (db.UniqueConstraint('type', 'from_pid', 'to_pid'),)

    def __init__(
            self,
            rtype,
            from_pid,
            to_pid,
            time_created=None,
            time_modified=None,
            time_removed=None):
        """
        Create a Relationship object.

        :param rtype: rtype constant
        :param from_pid: Person.id
        :param to_pid: Person.id
        :param time_created: datetime.datetime
        :param time_modified: datetime.datetime
        :param time_removed: datetime.datetime
        :return: None
        """
        if rtype not in Rtype:
            raise TypeError('Invalid Relationship type')
        self.type = rtype.value
        self.from_pid = from_pid
        self.to_pid = to_pid
        if time_created is not None:
            self.time_created = time_created
        if time_modified is not None:
            self.time_modified = time_modified
        if time_removed is not None:
            self.time_removed = time_removed