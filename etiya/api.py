from flask import Flask, jsonify, request
import sys
import os
from celery import Celery

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__),"..", "..",  "etiya")))

import algorithm

celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/train', methods=['GET'])
def train():
    # file = open('algorithm.py', 'r').read()
    # return exec(file)
    print("train called")
    result = algorithm.start()
    return result

@celery.task
@app.route('/prediction/<text>/', methods=['GET'])
def prediction(text):
    prediction = algorithm.prediction(text)
    print(prediction)
    print(type(prediction))
    return jsonify({'success': True,'prediction': prediction[0]})
app.run()

