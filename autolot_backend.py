from flask import Flask
from flask.ext.cqlalchemy import CQLAlchemy

app = Flask(__name__)
app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
app.config['CASSANDRA_SETUP_KWARGS'] = {'protocol_version': 3}


db = CQLAlchemy(app)


class User(db.Model):
    name = db.columns.Text(primary_key=True)


@app.route('/')
def hello_world():
    usr = User.create(username='John Doe')
    return usr


if __name__ == '__main__':
    db.sync_db()
    app.run(host='0.0.0.0', port=8000)
