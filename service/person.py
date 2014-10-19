"""
Person APIs
"""
__author__ = 'RAY'


import data.person
import people
db = people.db


def create_person(
        name,
        creator_id,
        birth=None,
        death=None):
    """
    Create a Person object and insert the row in the DB.

    :param name: string
    :param creator_id: Person.id foreign key
    :param birth: datetime.datetime
    :param death: datetime.datetime
    :return: Person object
    """
    person = data.person.Person(
        name,
        creator_id,
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
        birth=None,
        death=None):
    """
    Create a Person object for yourself (i.e., creator_id = id)

    :param name: string
    :param birth: datetime.datetime
    :param death: datetime.datetime
    :return: Person object
    """
    myself = create_person(name, DEFAULT_CREATOR, birth, death)
    myself.creator_id = myself.id
    db.session.add(myself)
    db.session.commit()
    return myself


def get_person(uid):
    """
    Retrieve a person by id.

    :param uid: user id
    :return: Person object
    """
    return data.person.Person.query.get(uid)