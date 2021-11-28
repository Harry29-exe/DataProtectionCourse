from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/<username>")
def get_username(username):
    print(username)

    return {}


app.run()
