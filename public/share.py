from flask import Blueprint, render_template, redirect, url_for


posts = Blueprint("posts", __name__)


@posts.route("/post")
def post():
    return render_template("editor.html")


@posts.route("/blog")
def blog():
    return render_template("blog.html")