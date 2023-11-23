from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required


posts = Blueprint("posts", __name__)


@posts.route("/post")
@login_required
def post():
    return render_template("editor.html")


@posts.route("/blog")
@login_required
def blog():
    return render_template("blog.html")
