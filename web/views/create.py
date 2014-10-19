"""
Web handlers for the create form.
"""
__author__ = 'RAY'

import data.relationship
import flask
import re
import service.person


def home():
    """
    Render the create form.

    :return: the form
    """
    relationship = flask.request.args.get('relationship')
    if relationship == str(data.relationship.Rtype.mom.value):
        relative = 'your mom'
    else:
        relative = 'yourself'
        relationship = None

    return flask.render_template(
        'create.html',
        relative=relative,
        relationship=relationship)


def validate_form():
    """
    Check the form inputs.

    :return: True/False whether the inputs are valid
    """
    if flask.request.form['name'] == '':
        return False

    date_re = '\d\d\d\d+-\d\d-\d\dT\d\d:\d\d'
    if not re.match(date_re, flask.request.form['birth']):
        return False
    death = flask.request.form.get('death')
    if (death is not None) and not re.match(date_re, death):
        return False

    #
    # TODO: validate relationship
    #
    return True


def person():
    """
    Use the form data to create a person.

    :return: redirect to the person page
    """
    if not validate_form():
        return flask.redirect(flask.url_for('create'))

    person = service.person.create_myself(
        flask.request.form['name'],
        birth = flask.request.form['birth'])

    #
    # TODO: create the relationship
    #
    return flask.redirect(flask.url_for('person', uid=person.id))