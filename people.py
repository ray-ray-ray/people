"""
Start the web server. Define routes and handlers here.
"""
import flask
import flask.ext.sqlalchemy


def create_app(config):
    """
    Instantiate the Flask app and the db.

    :param config: dict of config options
    :return: Flask app
    """
    app = flask.Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
    db = flask.ext.sqlalchemy.SQLAlchemy(app)
    return app, db


app, db = create_app({
    'SQLALCHEMY_DATABASE_URI': 'postgresql+psycopg2://localhost:5432/people'})


@app.route('/')
def hello_world():
    """
    Root handler to confirm server is up.

    :return: string
    """
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
