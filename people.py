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


@app.route('/')
def hello_world():
    """
    Root handler to confirm server is up.

    :return: string
    """
    return 'Hello World!'


@app.route('/create')
def create():
    """
    Render page to create a person

    :return: rendered template
    """
    return flask.render_template('create.html')


if __name__ == '__main__':
    app.run()
