from flask import Flask
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

@application.route("/")
def home():
    return "Hello!"

@application.route("/members")
def members():
    return {"Members": ["member1", "member2"]}

@application.route("/meals")
def meals():
    return {"meals": ["meal1", "meal2"]}

if __name__ == "__main__":
    application.run(debug=True)