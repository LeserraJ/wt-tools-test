from flask import Flask
from flask import render_template

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html', title = 'Test')



@app.route("/usa")
def usa_main():
    return render_template('usa_main.html', title = "USA Ground")


@app.route("/germany")
def germany_main():
    return render_template('germany_main.html', title = "Germany Ground")
# For hot reload CLI Command flask --app app --debug run