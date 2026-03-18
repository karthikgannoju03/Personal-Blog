from flask import render_template
from app.main import main
from app.models import Post

@main.route("/")
def index():

    posts = Post.query.all()

    return render_template("index.html", posts=posts)