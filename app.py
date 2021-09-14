from flask import Flask,jsonify,request
from classifier import getPrediction

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

if(__name__ == "__main__"):
    app.run(debug=True)

