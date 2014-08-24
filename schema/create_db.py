"""
Builds the DB based on SQLAlchemy models.
"""
__author__ = 'RAY'

#
# Must import this to get the models
#
import data.person
import people

if __name__ == '__main__':
    db = people.db
    db.drop_all()
    db.create_all()
    db.session.commit()
