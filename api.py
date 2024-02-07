from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

import json





app = Flask(__name__)


# Load the data from the JSON file
with open("tanks_data.json", "r") as json_file:
    tanks_data = json.load(json_file)







@app.route('/', methods=['GET'])
def get_tanks():
    return jsonify(tanks_data)


#@app.route('/tanks', methods=['POST'])
#def add_tank():
    #tanks.append(request.get_json())
    #return '', 204



if __name__ == "__main__":
    # Run the Flask app
    app.run(host='localhost', port=8080, debug=True)

