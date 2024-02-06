from flask import Flask, jsonify
import json





app = Flask(__name__)

app.run(host='0.0.0.0', port=8080, debug=True)
# Load the data from the JSON file
with open("tanks_data.json", "r") as json_file:
    tanks_data = json.load(json_file)

@app.route('/api/tanks', methods=['GET'])
def get_tanks():
    return jsonify(tanks_data)

if __name__ == '__main__':
    app.run(debug=True)
