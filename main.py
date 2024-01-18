import flask
import random
import time

app = flask.Flask(__name__)


@app.route("/")
def index():
    return f'{random.random()}'


app.run(debug=True)
