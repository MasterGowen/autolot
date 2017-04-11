from flask import Flask
from flask.ext.cqlalchemy import CQLAlchemy

app = Flask(__name__)
app.config.from_object('config_dev')


db = CQLAlchemy(app)


class User(db.Model):
    __keyspace__ = 'test'
    name = db.columns.Text(primary_key=True)


@app.route('/')
def hello_world():
    usr = User.create(username='John Doe')
    return usr


if __name__ == '__main__':
    db.sync_db()
    app.run(host='0.0.0.0', port=8000)
