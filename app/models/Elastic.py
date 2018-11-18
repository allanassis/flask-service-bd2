import requests
from elasticsearch import Elasticsearch

import app.settings as settings


class Elastic(Elasticsearch):

    def __init__(self, domain, port):
        Elasticsearch.__init__(self, [{'host': domain, 'port': port}])

    def getDoc(self, ident, query=None):
        res = self.get(settings.index, settings.doc_type, ident, query)
        return res

    def insert(self, document):
        res = self.index(settings.index, settings.doc_type, document)
        return res
