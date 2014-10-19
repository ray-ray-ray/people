"""
Web handlers for the create form.
"""
__author__ = 'RAY'

import flask
import service.person


def home():
    """
    Render the create form.

    :return: the form
    """
    return flask.render_template('create.html')


def myself():
    """
    Use the form data to create a person.

    :return: redirect to the person page
    """
    #
    # verify the form data
    #
    if flask.request.form['name'] == '':
        return flask.render_template('create.html', error='Please enter a name')

    person = service.person.create_myself(flask.request.form['name'])
    return flask.redirect(flask.url_for('person', uid=person.id))