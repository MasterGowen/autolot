app.config['CASSANDRA_HOSTS'] = ['127.0.0.1']
app.config['CASSANDRA_KEYSPACE'] = "test"
app.config['CASSANDRA_SETUP_KWARGS'] = {'protocol_version': 3}