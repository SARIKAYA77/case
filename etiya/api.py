import flask
import sys
import os
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__),"..", "..",  "etiya")))

import algorithm  # noqa


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/train', methods=['GET'])
def train():
    file = open('algorithm.py', 'r').read()
    print("train called")
    return exec(file)
    # return "<h1>this endpoint train algorithm.</p>"

@app.route('/prediction', methods=['GET'])
def prediction():
    # data = request.get_json()
    return "<h1>this endpoint prediction algorithm.</p>"
app.run()

