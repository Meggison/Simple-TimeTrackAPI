import os  # Import the os module
from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

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
    current_time = datetime.datetime.now(pytz.utc)
    current_time_str = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

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
    app.run()