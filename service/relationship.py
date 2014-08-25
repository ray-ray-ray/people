"""
Relationship APIs
"""
__author__ = 'RAY'


import data.relationship
import people
db = people.db


def create_relationship(rtype, from_pid, to_pid):
    """
    Create a uni-directional relationship between two people.

    :param rtype: data.relationship.Rtype
    :param from_pid: person.id
    :param to_pid: person.id
    :return: Relationship object
    """
    relationship = data.relationship.Relationship(rtype, from_pid, to_pid)
    db.session.add(relationship)
    db.session.commit()
    return relationship