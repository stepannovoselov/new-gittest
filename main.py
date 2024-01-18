import flask
import random

app = flask.Flask(__name__)


@app.route("/")
def index():
    return f'{random.random()} | {random.random()}'


app.run(debug=True)
