"""
Start the web server. Define routes and handlers here.
"""
__author__ = 'RAY'


import flask
import flask.ext.sqlalchemy
import os


app = flask.Flask(__name__, template_folder='web/templates')
app.config.from_object(os.getenv('FLASKCONFIG', 'config.default.Config'))
db = flask.ext.sqlalchemy.SQLAlchemy(app)


#
# These require db to exist.
#
import web.views.create
import web.views.person


@app.route('/')
def hello_world():
    """
    Root handler to confirm server is up.

    :return: string
    """
    return 'Hello World!'


@app.route('/create', methods=['GET', 'POST'])
def create():
    """
    Route to the creation form or handle the form data.

    :return: rendered template
    """
    if flask.request.method == 'GET':
        return web.views.create.home()
    elif flask.request.method == 'POST':
        return web.views.create.myself()


@app.route('/person/<uid>')
def person(uid=None):
    """
    Render this person.

    :param uid: user id
    :return: rendered person page
    """
    return web.views.person.home(uid=uid)


if __name__ == '__main__':
    app.run()
