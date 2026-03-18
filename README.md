# 🌟 Personal Blog 

## 📌 Project Description

This project is a simple personal blog web application built using Flask. It allows users to register, login, create blog posts, and comment on posts.

---

## 🚀 Features

- User Registration & Login
- Create Blog Posts
- View All Posts
- Comment System
- SQLite Database
- Flask Blueprints Structure
- Jinja2 Templates
- Static CSS Styling

---

## 🛠️ Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- SQLite
- HTML, CSS

---


## 📂 Project Structure

Personal-Blog/
├── app/
│   ├─ __init__.py
│   ├─ models.py
│   ├─ auth/
│   │   ├─ __init__.py
│   │   ├─ routes.py
│   │   └─ forms.py
│   ├─ main/
│   │   ├─ __init__.py
│   │   └─ routes.py
│   ├─ posts/
│   │   ├─ __init__.py
│   │   ├─ routes.py
│   │   └─ forms.py
│   ├─ comments/
│   │   ├─ __init__.py
│   │   └─ routes.py
│   ├─ static/
│   │   └─ css/
│   │       └─ style.css
│   └─ templates/
│       ├─ base.html
│       ├─ index.html
│       ├─ login.html
│       ├─ register.html
│       ├─ create_post.html
│       └─ post.html
├─ config.py
├─ run.py
├─ requirements.txt
├─ .gitignore
└─ README.md
---

## ⚙️ Setup Instructions

1. Clone repository

2. Create virtual environment

3. Activate environment

4. Install dependencies

5. Run project

6. Open browser

---

## 🗄️ Database Setup

Run Python shell:

```python
from app import create_app, db
app = create_app()
app.app_context().push()
db.create_all()
