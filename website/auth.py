from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<h>Login</h>"

@auth.route('/logout')
def logout():
    return "<h>Logout</h>"

@auth.route('/sign-up')
def sign_up():
    return "<h>Signu Up</h>"