from flask import Flask, request, render_template
from pymongo import MongoClient
from datetime import datetime
from prometheus_flask_exporter import PrometheusMetrics
import os


app = Flask(__name__)


metrics = PrometheusMetrics(app, group_by='endpoint')
metrics.info('app_info', 'Application info', version='1.0.3')


mongo_uri = os.environ.get('MONGO_URI')
# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client['users']  # Use 'users' database

@app.route('/', methods=['GET', 'POST'])
@metrics.histogram(
    'requests_by_status_and_path', 'Request latencies by status and path', labels={
        'status': lambda r: r.status_code, 'path': lambda: request.path})
def index():
    if request.method == 'POST':
        name = request.form['name']
        timestamp = datetime.now()
        # Inserting data into MongoDB
        db.users.insert_one({'name': name, 'timestamp': timestamp})
        return 'Name "{}" added to the database with timestamp: {}'.format(name, timestamp)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=False)
