from flask import request, redirect
from app.comments import comments
from app.models import Comment
from app import db

@comments.route("/add/<int:post_id>", methods=["POST"])
def add_comment(post_id):

    text = request.form["content"]

    comment = Comment(content=text, post_id=post_id)

    db.session.add(comment)
    db.session.commit()

    return redirect("/")