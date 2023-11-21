from flask import Blueprint, render_template

log = Blueprint("log", __name__)

@log.route("/login", strict_slashes=False)
def login():
    return render_template("login.html")

@log.route("/signup", strict_slashes=False)
def signup():
    return render_template("signup.html")
