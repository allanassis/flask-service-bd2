from flask import Flask, request
from app.models.Elastic import Elastic
import json

app = Flask(__name__)
es = Elastic("localhost", 9200)


@app.route("/", methods=["GET"])
def get():
    import pdb
    pdb.set_trace()
    identifier = json.loads(request.data)
    return json.dumps(es.getDoc(identifier["id"]))


@app.route("/", methods=["POST"])
def post():
    body = json.loads(request.data)
    document = es.insert(body)
    return json.dumps(document)
