"""
Builds the DB based on SQLAlchemy models.d
"""
__author__ = 'RAY'


import people
#
# Required import to load the data models into people.db
#
import data.person


if __name__ == '__main__':
    db = people.db
    db.drop_all()
    db.create_all()
    db.session.commit()
