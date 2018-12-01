import requests
import re
from elasticsearch import Elasticsearch

import app.settings as settings


class Elastic(Elasticsearch):

    def __init__(self, domain):
        auth = self._get_auth()
        host = self._get_host(auth)
        es_header = [{
            'host': host,
            'port': 443,
            'use_ssl': True,
            'http_auth': (auth[0], auth[1])
        }]
        Elasticsearch.__init__(self, es_header)

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

    def _get_auth(self):
        return re.search('https\:\/\/(.*)\@',
                         settings.host).group(1).split(':')

    def _get_host(self, auth):
        return settings.host.replace('https://%s:%s@' % (auth[0], auth[1]), '')
