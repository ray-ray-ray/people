"""
Start the web server. Define routes and handlers here.
"""
__author__ = 'RAY'


import flask
import flask.ext.login
import flask.ext.sqlalchemy
import os

#
# Flask app, db, and login setup
#
app = flask.Flask(__name__, template_folder='web/templates')
app.config.from_object(os.getenv('FLASKCONFIG', 'config.default.Config'))
db = flask.ext.sqlalchemy.SQLAlchemy(app)
login_manager = flask.ext.login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


#
# These require db to exist.
#
import service.user
import web.views.create
import web.views.home
import web.views.login
import web.views.person


@login_manager.user_loader
def user_loader(uid):
    """
    Get a user for the login manager.

    :param uid: User.id
    :return: the user object
    """
    return service.user.get_user(uid)


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Render the login form and handle it.

    :return: rendered template
    """
    if flask.request.method == 'GET':
        return web.views.login.home()
    elif flask.request.method == 'POST':
        return web.views.login.login()


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
