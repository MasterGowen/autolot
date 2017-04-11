import uuid

from flask import Flask
from flask.ext.cqlalchemy import CQLAlchemy

app = Flask(__name__)
app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
app.config['CASSANDRA_KEYSPACE'] = "test"
app.config['CASSANDRA_SETUP_KWARGS'] = {'protocol_version': 3}


db = CQLAlchemy(app)


class User(db.Model):
    __keyspace__ = 'test'
    id = db.columns.UUID(primary_key=True, default=uuid.uuid4)
    name = db.columns.Text(primary_key=False)


@app.route('/', methods=['GET'])
def hello_world():
    usr = None
    for i in range(1000):
        usr = User(name='John Doe ' + str(i))
        usr.save()
    return str(usr)


if __name__ == '__main__':
    db.sync_db()
    app.run(host='0.0.0.0', port=8000)
