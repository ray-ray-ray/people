"""
Web handlers for the create form.
"""
__author__ = 'RAY'

import flask
import httplib
import re
import service.person
import service.user


def home():
    """
    Render the create form.

    :return: the form
    """
    return flask.render_template('create.html')


def validate_form():
    """
    Check the form inputs.

    :return: True/False whether the inputs are valid
    """
    if flask.request.form['name'] == '':
        return False
    if flask.request.form['email'] == '':
        return False
    if flask.request.form['password'] == '':
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


def myself():
    """
    Use the form data to create the current user.

    :return: redirect to the person page
    """
    if not validate_form():
        flask.abort(httplib.BAD_REQUEST)

    me = service.person.create_myself(
        flask.request.form['name'],
        birth=flask.request.form['birth'])
    service.user.create_user(
        me.id,
        flask.request.form['email'],
        flask.request.form['password'])

    #
    # TODO: implement Flask-login
    #
    return flask.redirect(flask.url_for('person', uid=me.id))