from flask import Flask, jsonify, request #,render_template

import json





app = Flask(__name__)

# Load the data from the JSON file

with open("tanks_data.json", "r") as json_file:
    tanks_data = json.load(json_file)

@app.route("/")
def get_tanks():
    return jsonify(tanks_data)









if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)