# TimeTrackAPI Documentation

## Overview

This Flask application provides a simple web server with two endpoints. It demonstrates basic functionalities including serving a static message, handling GET requests with query parameters, and returning JSON responses. The application includes features like current day and time retrieval, as well as constructing GitHub URLs.

## Requirements

- Python 3.x
- Flask
- pytz

## Installation

1. Clone the repository:
2. Navigate to the cloned directory and install dependencies:
pip install Flask pytz

## Usage

### Running the Server

Execute the following command to start the Flask server:
python app.py


By default, the server runs on port 5000, but this can be modified using the `PORT` environment variable.

### Endpoints

1. **Hello Endpoint (`/`):** 
   - Returns a simple greeting.
   - Usage: Access `[host URL]/`.

2. **API Endpoint (`/api`):**
   - Accepts GET requests with optional query parameters: `slack_name` and `track`.
   - Returns a JSON response containing the slack_name, current day, current UTC time, track, and URLs for a GitHub repository and file.
   - Usage: Access `[host URL]/api?slack_name=[name]&track=[track]`.

### Example Request
url -X GET '[host URL]/api?slack_name=JohnDoe&track=DataScience


## Configuration

- **Port Configuration:**
  The application uses the `PORT` environment variable. If not set, it defaults to port 5000.

- **Time Zone:**
  The application is set to use the 'US/Eastern' timezone for retrieving the current day.

- **GitHub URLs:**
  Modify the `github_repo_url` and `github_file_url` in the `/api` endpoint as per your repository details.


