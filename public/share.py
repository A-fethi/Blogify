from flask import Blueprint, render_template

share = Blueprint("share", __name__)

@share.route("/post", strict_slashes=False)
def post():
    return render_template("blog.html")

@share.route("/create", strict_slashes=False)
def create():
    return render_template("editor.html")
