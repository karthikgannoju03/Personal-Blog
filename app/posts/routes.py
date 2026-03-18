from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app.posts import posts
from app.posts.forms import PostForm
from app.models import Post
from app import db

@posts.route("/create", methods=["GET","POST"])
@login_required
def create_post():

    form = PostForm()

    if form.validate_on_submit():

        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user
        )

        db.session.add(post)
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template("create_post.html", form=form)