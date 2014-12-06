import rdflib
import json
import random


jsonldData = open("AutomaticItemGenerationOntologyExpanded.jsonld", 'r').read()
queryData = open("getItem.query", 'r').read()

graph = rdflib.Graph()
graph.parse( data = jsonldData , format = 'json-ld' )

result = graph.query( queryData )

for row in result:
    ( name, age, status, minMandatorySymptoms, minOptionalSymptoms, optionalSymptoms, mandatorySymptoms ) = row
    optionalSymptoms = json.loads(optionalSymptoms.replace(",None", ""))
    mandatorySymptoms = json.loads(mandatorySymptoms.replace("None,", ""))
    numberOptionalSymptoms = random.randint( int(minOptionalSymptoms), len(optionalSymptoms))
    numberMandatorySymptoms = random.randint( int(minMandatorySymptoms), len(mandatorySymptoms))

mandatorySymptoms = list(mandatorySymptoms.items())
optionalSymptoms = list(optionalSymptoms.items())

print( name + ', ' + age + ' years, ' + status, end='. ' )
for n in range( numberMandatorySymptoms ):
    print( mandatorySymptoms[n][1], end='. ' )
for n in range( numberOptionalSymptoms ):
    print( optionalSymptoms[n][1], end='. ' )
