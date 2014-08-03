"""
Start the web server. Define routes and handlers here.
"""
import flask
import flask.ext.sqlalchemy

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://localhost:5432/people'
db = flask.ext.sqlalchemy.SQLAlchemy(app)


@app.route('/')
def hello_world():
    """
    Root handler to confirm server is up.

    :return: string
    """
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
