## Usage

`pipenv install`

## Running tests

`pipenv run pytest`

## Running python development server

`pipenv run python main.py`

## Frontend Requirements

- [ ] new react-based browser frontend using modern best practice tooling
      (whatever that means to you) (MVP)
- [ ] display a list of articles by title (MVP)
- [ ] mobile-first responsive design (MVP)
- [ ] meets basic accessibility requirements (MVP)
- [ ] unit and/or integration tests (MVP)
- [ ] display an article's details (M1)
- [ ] display an author's details (M1)
- [ ] link article to author (M1)
- [ ] anonymous user can edit article details (M2)


## Backend Requirements

- [ ] implement the endpoint(s) needed to power the frontend in python/flask
      (MVP)
- [ ] write a Dockerfile for deploying the application in (a) container(s)
      (M1)
- [ ] create a CI pipeline for the whole application (M1)
- [ ] associate multiple authors with an article (M2)


## Useful documentation

* Querying records in `flask_sqlalchemy`: https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#querying-records
* Accessing request params in `flask`: http://flask.pocoo.org/docs/1.0/quickstart/#the-request-object
* Creating json responses in `flask`: http://flask.pocoo.org/docs/1.0/api/#flask.json.jsonify
