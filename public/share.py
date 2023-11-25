from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import Post, User
from . import db

posts = Blueprint("posts", __name__)


@posts.route("/post", methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        title = request.form.get('title')
        article = request.form.get('article')

        if not article:
            flash('Post cannot be empty', category='error')
        elif not title:
            flash('Title cannot be empty', category='error')
        else:
            post = Post(title=title, article=article, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post Created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("editor.html", user=current_user)


@posts.route("/blog/<id>")
@login_required
def blog(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash("Post Does Not Exist", category='error')
        return redirect(url_for('views.home'))
    return render_template("blog.html", user=current_user, post=post)
    

@posts.route("/delete/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        flash("Post Does Not Exist", category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post Deleted!', category='success')
        return redirect(url_for('views.home'))
    return render_template("index.html", user=current_user)
