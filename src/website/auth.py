from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<p>Login page placeholder</p>"


@auth.route('/logout')
def logout():
    return "<p>Logout page placeholder</p>"


@auth.route('/register')
def register():
    return "<p>Register page placeholder</p>"
