"""
Start the web server. Define routes and handlers here.
"""
__author__ = 'RAY'


import flask
import flask.ext.security
import flask.ext.sqlalchemy
import os

#
# Flask app and db
#
app = flask.Flask(__name__, template_folder='web/templates')
app.config.from_object(os.getenv('FLASKCONFIG', 'config.default.Config'))
db = flask.ext.sqlalchemy.SQLAlchemy(app)

#
# Setup Flask-Security
#
import data.role
import data.user
user_datastore = flask.ext.security.SQLAlchemyUserDatastore(
    db,
    data.user.User,
    data.role.Role)
security = flask.ext.security.Security(app, user_datastore)

#
# These require db to exist.
#
import web.views.create
import web.views.home
import web.views.login
import web.views.person


@app.route('/')
def home():
    """
    Root handler to confirm server is up.

    :return: rendered template
    """
    return web.views.home.home()


@app.route('/create', methods=['GET', 'POST'])
def create():
    """
    Route to the creation form or handle the form data.

    :return: rendered template or redirect
    """
    if flask.request.method == 'GET':
        return web.views.create.home()
    elif flask.request.method == 'POST':
        return web.views.create.myself()


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     """
#     Render the login form and handle it.
#
#     :return: rendered template
#     """
#     if flask.request.method == 'GET':
#         return web.views.login.home()
#     elif flask.request.method == 'POST':
#         return web.views.login.login()


@app.route('/person/<uid>')
def person(uid):
    """
    Render this person.

    :param uid: user id
    :return: rendered person page
    """
    return web.views.person.home(uid)


if __name__ == '__main__':
    app.run()
