import os
index = os.getenv('index', 'papers')
doc_type = os.getenv('doc_type', 'paper')
host = os.getenv('elastic_host', 'localhost:9200')
