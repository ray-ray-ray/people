__author__ = 'RAY'


import datetime
import people
db = people.db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    mom_id = db.Column(db.Integer)
    dad_id = db.Column(db.Integer)
    creator_id = db.Column(db.Integer, nullable=False)
    birth = db.Column(db.DateTime(timezone=True))
    death = db.Column(db.DateTime(timezone=True))
    time_created = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now, nullable=False)
    time_modified = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)
    time_removed = db.Column(db.DateTime(timezone=True))