from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/members")
def members():
    return {"Members": ["member1", "member2"]}

if __name__ == "__main__":
    app.run(debug=True)