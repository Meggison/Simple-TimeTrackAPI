import os
from flask import Flask, request, jsonify
import datetime
import pytz
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set the Postgres database URL directly here
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ivhfdisaapirgd:65fb77e5489d510ddb43657b978a4356dfb73ce0131c9ef0693362c5e170132a@ec2-52-0-79-72.compute-1.amazonaws.com:5432/dfadpvek5s2jkd'

db = SQLAlchemy(app)

# Get the port from the environment variable or use 5000 as a default
port = int(os.environ.get("PORT", 5000))

# Define Person model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(100), nullable=True)

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()


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
    current_time_str = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

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

# CREATE a new person
@app.route('/api/persons', methods=['POST'])
def create_person():
    data = request.get_json()
    new_person = Person(name=data['name'], age=data['age'], email=data['email'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'person_id': new_person.id}), 201

# READ a person by ID
@app.route('/api/persons/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = Person.query.get(person_id)
    if person is None:
        return jsonify({'message': 'Person not found'}), 404
    return jsonify({
        'id': person.id,
        'name': person.name,
        'age': person.age,
        'email': person.email
    })

# UPDATE a person by ID
@app.route('/api/persons/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    data = request.get_json()
    person = Person.query.get(person_id)
    if person is None:
        return jsonify({'message': 'Person not found'}), 404
    person.name = data['name']
    person.age = data['age']
    person.email = data['email']
    db.session.commit()
    return jsonify({'message': 'Person updated'})


# DELETE a person by ID
@app.route('/api/persons/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get(person_id)
    if person is None:
        return jsonify({'message': 'Person not found'}), 404
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted'})


if __name__ == '__main__':
    # Use the PORT environment variable provided by Heroku
    create_tables()
    app.run(host="0.0.0.0", port=port)
