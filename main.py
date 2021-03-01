from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import pytest
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
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
Tests
"""


@pytest.fixture(scope="function")
def session(request):
    """Creates a new database session for a test."""
    db.create_all()

    def teardown():
        db.drop_all()

    request.addfinalizer(teardown)
    return db.create_scoped_session()


@pytest.fixture
def client():
    return app.test_client()


def test_articles(session, client):
    jane = Author(firstname="Jane", lastname="Doe")
    brief = Article(title="A brief history", author=jane)
    session.add(brief)
    session.commit()
    response = client.get("/articles.json")
    assert json.loads(response.data) == [
        {"author": {"firstname": "Jane", "lastname": "Doe"}, "title": "A brief history"}
    ]


# Uncomment the following line to skip this test
# @pytest.mark.skip()
def test_article_by_id(session, client):
    jane = Author(firstname="Jane", lastname="Doe")
    brief = Article(title="A brief history", author=jane)
    session.add(brief)
    session.commit()
    response = client.get("/article.json?id=%i" % (brief.id))
    assert json.loads(response.data) == {
        "author": {"firstname": "Jane", "lastname": "Doe"},
        "title": "A brief history",
    }


if __name__ == "__main__":
    pytest.main(["main.py"])
