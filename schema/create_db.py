__author__ = 'RAY'


import people
import data.person


if __name__ == '__main__':
    db = people.db
    db.drop_all()
    db.create_all()
    db.session.commit()

