import flask
import random

app = flask.Flask(__name__)


@app.route("/")
def index():
    return f'{random.random()} | {random.random()} | <a href="/login">олфл</a>'


@app.route("/login")
def login():
    return open('index.html').read()


app.run(port=1488, debug=True)
