"""
Handlers for the person page.
"""
__author__ = 'RAY'

import data.relationship
import flask
import service.person


def home(uid):
    """
    Render a person.

    :param uid: user id
    :param is_self: whether this person is the current user
    :return: person page
    """
    person = service.person.get_person(uid)
    creator = service.person.get_person(person.creator_id)
    return flask.render_template(
        'person.html',
        name = person.name,
        birth = person.birth,
        death = person.death,
        uid = person.id,
        creator_id = creator.id,
        creator_name = creator.name,
        time_created = person.time_created,
        momtype = data.relationship.Rtype.mom.value,
        dadtype = data.relationship.Rtype.dad.value)