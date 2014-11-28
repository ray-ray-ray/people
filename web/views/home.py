"""
Web handlers to render the homepage.
"""
__author__ = 'RAY'

import flask


def home():
    return flask.render_template('home.html')