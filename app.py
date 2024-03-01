from flask import Flask, request, render_template
from pymongo import MongoClient
from datetime import datetime
import os
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics

app = Flask(__name__)

mongo_uri = os.environ.get('MONGO_URI')
# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client['users']  # Use 'users' database

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        timestamp = datetime.now()
        # Inserting data into MongoDB
        db.users.insert_one({'name': name, 'timestamp': timestamp})
        return 'Name "{}" added to the database with timestamp: {}'.format(name, timestamp)
    return render_template('index.html')


# provide app's version and deploy environment/config name to set a gauge metric
register_metrics(app, app_version="v0.1.2", app_config="staging")

# Plug metrics WSGI app to your main app with dispatcher
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

run_simple(hostname="0.0.0.0", port=5000, application=dispatcher)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port='5000', debug=True)

