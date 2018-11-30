import requests
from elasticsearch import Elasticsearch

import app.settings as settings


class Elastic(Elasticsearch):

    def __init__(self, domain, port):
        Elasticsearch.__init__(self, [{'host': domain, 'port': port}])

    def get_doc(self, identifier):
        try:
            return self.get(settings.index, settings.doc_type, id=identifier)
        except:
            return "Document not found"

    def get_all_doc(self):
        return self.search(index=settings.index, body={"query": {"match_all": {}}})

    def insert_doc(self, document):
        res = self.index(settings.index, settings.doc_type, document)
        return res

    def update_doc(self, identifier, document):
        return self.update(settings.index, settings.doc_type, id=identifier, body=document)
