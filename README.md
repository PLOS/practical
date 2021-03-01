## Usage

`pipenv install`

## Running tests

`pipenv run python main.py`

## TODO

- [ ] Implement `/articles.json` endpoint. Should return all all articles
- [ ] Implement `/article.json?id=123` endpoint. Should return a single article
- [ ] Implement `/articles.json?author_id=123` endpoint. Should return all articles by an author
- [ ] Change database schema to allow multiple authors per article

## Useful documentation

* Querying records in `flask_sqlalchemy`: https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#querying-records
* Accessing request params in `flask`: http://flask.pocoo.org/docs/1.0/quickstart/#the-request-object
* Creating json responses in `flask`: http://flask.pocoo.org/docs/1.0/api/#flask.json.jsonify
