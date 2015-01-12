"""
User APIs
"""
__author__ = 'RAY'


import data.user
import people
db = people.db


def create_user(pid, email, password):
    """
    Create a user.

    :param pid: Person.id
    :param email: email address
    :param password: encrypted password
    :return: User object
    """
    user = data.user.User(pid, email, password, True)
    db.session.add(user)
    db.session.commit()
    return user


def get_user(uid):
    """
    Retrieve a user by id.

    :param uid: User.id
    :return: data.user.User
    """
    return data.user.User.query.get(uid)


def login(email, password):
    """
    Login the user after checking the credentials.

    :param email: email address
    :param password: password
    :return: whether the login was successful
    """
    user = data.user.User.query.filter_by(
        email=email,
        password=password).first()
    if user is None:
        return False
    else:
        flask.ext.login.login_user(user)
        return True