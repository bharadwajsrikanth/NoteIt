from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<p>Login page placeholder</p>"


@auth.route('/logout')
def logout():
    return "<p>Logout page placeholder</p>"


@auth.route('/register')
def register():
    return render_template("register.html")
