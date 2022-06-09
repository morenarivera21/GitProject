from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)
persons = []


@app.route("/persons", methods=['POST'])
def dummy_example():
    print(request.json)
    print(request.method)
    print(request.url)
    print(request.data)

    return request.json





