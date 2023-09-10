import os
from flask import Flask, request, jsonify
import datetime
import pytz
import random

app = Flask(__name__)

def get_current_utc_time():
    current_time = datetime.datetime.utcnow()
    # Generate a random time interval within +/-2 minutes (120 seconds)
    random_seconds = random.randint(-120, 120)
    adjusted_time = current_time + datetime.timedelta(seconds=random_seconds)
    return adjusted_time

@app.route('/')
def hello():
    return 'hello'

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.datetime.now(pytz.utc).astimezone(pytz.timezone('US/Eastern')).strftime("%A")

    # Get current UTC time with validation of +/-2 minutes
    current_time = get_current_utc_time()
    current_time_str =  current_time.strftime('%Y-%m-%dT%H:%M:%SZ')


    # Construct GitHub URLs
    github_repo_url = "https://github.com/username/repo"
    github_file_url = github_repo_url + "/blob/main/file_name.ext"

    # Prepare JSON response
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time_str,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response)

if __name__ == '__main__':
    # Use the PORT environment variable provided by Heroku
    app.run(debug=True)