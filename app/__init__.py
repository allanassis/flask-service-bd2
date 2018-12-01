from flask import Flask, request
from app.models.Elastic import Elastic
import app.settings as settings
import json

app = Flask(__name__)
es = Elastic(settings.host)


@app.route("/", methods=["GET"])
def get():
    if not len(request.args):
        return json.dumps(es.get_all_doc())
    identifier = request.args['id']
    return json.dumps(es.get_doc(identifier))


@app.route("/", methods=["POST"])
def post():
    body = json.loads(request.data)
    document = es.insert_doc(body)
    return json.dumps(document)


@app.route("/", methods=["PUT"])
def put():
    if not len(request.args):
        return "You must specify the id"
    if not len(request.data):
        return "Not modified"
    body = {"doc": json.loads(request.data)}
    identifier = request.args['id']
    document = es.update_doc(identifier, body)
    return json.dumps(document)
