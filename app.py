from flask import Flask, render_template, request
import pymongo
import urllib.parse

app = Flask(__name__)

# Replace <password> with your MongoDB password
password = "CanSinal1190"

# Escape the username and password
username = urllib.parse.quote_plus("mongo")
password = urllib.parse.quote_plus(password)

# Set up the MongoDB client
connection_string = f"mongodb+srv://{username}:{password}@injuries.zu80i6x.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_string)

# Access your database and collection
db = client.test
collection = db.injuries

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table')
def table():
    injuries = [...]  # get injury data from database or other source
    return render_template('table.html', injuries=injuries)


@app.route('/submit', methods=['POST'])
def submit():
    # Get the form data
    player_name = request.form.get('name')
    injury_type = request.form.get('injury-type')
    date = request.form.get('date')
    description = request.form.get('description')

    # Insert the data into the database
    injury = {
        "player_name": player_name,
        "injury_type": injury_type,
        "date": date,
        "description": description
    }
    collection.insert_one(injury)

    return {'success': True}

if __name__ == '__main__':
    app.run(debug=True)
