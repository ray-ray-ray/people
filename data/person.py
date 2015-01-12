"""
Data model for Person
"""
__author__ = 'RAY'


import datetime
import people
db = people.db


class Person(db.Model):
    """
    SQLAlchemy object for Person
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    creator_id = db.Column(
        db.Integer,
        db.ForeignKey('person.id'),
        nullable=False)
    birth = db.Column(db.DateTime(timezone=True))
    death = db.Column(db.DateTime(timezone=True))
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

    def __init__(
            self,
            name,
            creator_id,
            birth=None,
            death=None,
            time_created=None,
            time_modified=None,
            time_removed=None):
        """
        Create a Person object which is basically Person row.

        :param name: string
        :param creator_id: Person.id foreign key
        :param birth: datetime.datetime
        :param death: datetime.datetime
        :param time_created: datetime.datetime
        :param time_modified: datetime.datetime
        :param time_removed: datetime.datetime
        :return: None
        """
        self.name = name
        self.creator_id = creator_id
        if birth is not None:
            self.birth = birth
        if death is not None:
            self.death = death
        if time_created is not None:
            self.time_created = time_created
        if time_modified is not None:
            self.time_modified = time_modified
        if time_removed is not None:
            self.time_removed = time_removed

    def __repr__(self):
        """
        String representation

        :return: <Person RAY Courtney>
        """
        return '<Person %r>' % self.name