"""
Web handlers to render the homepage.
"""
__author__ = 'RAY'

import flask


def home():
    """
    Render the homepage

    :return: rendered template
    """
    return flask.render_template('home.html')