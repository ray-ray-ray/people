"""
Builds the DB based on SQLAlchemy models.
"""
__author__ = 'RAY'

#
# Must import these to get the models
#
import data.person
import data.relationship
import data.role
import data.user
import data.user_role

import people

if __name__ == '__main__':
    db = people.db
    user_datastore = people.user_datastore
    db.drop_all()
    db.create_all()
    #user_datastore.create_user(email='ray@ray.com', password='password')
    db.session.commit()
