"""
Web handlers for the login form.
"""
__author__ = 'RAY'


import flask
import httplib
import service.person


def home():
    """
    Render the login form.

    :return: the form
    """
    return flask.render_template('login.html')


def login():
    """
    Login the user.

    :return: redirect to home
    """
    #
    # TODO: validate form inputs
    #
    if service.person.login(
            flask.request.form['email'],
            flask.request.form['password']):
        return flask.redirect('/')
    else:
        flask.abort(httplib.UNAUTHORIZED)