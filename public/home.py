from flask import Blueprint, render_template

home = Blueprint("home", __name__)

@home.route("/", strict_slashes=False)
@home.route("/home", strict_slashes=False)
def home():
    return render_template("index.html")
