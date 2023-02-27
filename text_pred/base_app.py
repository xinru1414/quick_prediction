from flask import Flask, render_template, request
from predictor import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello', methods=["post"])
def hello():
    req = request.json
    ans = predict(req['name'])
    return f"The label for seq {req['name']} is {ans}"
