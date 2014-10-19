"""
Handlers for the person page.
"""
__author__ = 'RAY'

import flask
import service.person


def home(uid=None):
    """
    Render a person.

    :param uid: user id
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
        time_created = person.time_created)