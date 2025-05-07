import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///practical.sql"
app.config["TESTING"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

"""
Data models
"""


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(), nullable=False)
    lastname = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return "<Author %s, %s>" % (self.lastname, self.firstname)

    def as_dict(self):
        return {"lastname": self.lastname, "firstname": self.firstname}


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)
    author = db.relationship("Author", backref=db.backref("articles", lazy=True))

    def __repr__(self):
        return "<Article %s (%r)>" % (self.title, self.author)

    def as_dict(self):
        return {"title": self.title, "author": self.author.as_dict()}


"""
Flask endpoints
"""

@app.route("/articles.json")
def articles():
    """Implement this first."""
    raise Exception("please implement")


@app.route("/article.json")
def article():
    """Implement this second."""
    raise Exception("please implement")


"""
Flask application
"""

if __name__ == "__main__":
    if not os.path.isfile("practical.sql"):
        with app.app_context():
            db.create_all()
    app.run()
