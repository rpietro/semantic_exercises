import jsonld
import json

data = json.load( open('diseases.jsonld'))

print data['@context']
print data['@graph']

compacted = jsonld.compact( data['@graph'] , data['@context'] )
