__author__ = 'RAY'


import data.person
import people
db = people.db


def create_person(
    name,
    creator_id,
    mom_id = None,
    dad_id = None,
    birth = None,
    death = None):
    person = data.person.Person(
        name,
        creator_id,
        mom_id,
        dad_id,
        birth,
        death)
    db.session.add(person)
    db.session.commit()
    return person


#
# Temporary creator_id when creating oneself.
#
DEFAULT_CREATOR = 0


def create_myself(
    name,
    mom_id = None,
    dad_id = None,
    birth = None,
    death = None):
    myself = create_person(name, DEFAULT_CREATOR, mom_id, dad_id, birth, death)
    myself.creator_id = myself.id
    db.session.add(myself)
    db.session.commit()
    return myself