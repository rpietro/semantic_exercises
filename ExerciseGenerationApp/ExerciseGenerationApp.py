import rdflib

jsonldFile = open('MajorDepressiveDisorderUseCaseExpanded.jsonld', 'r')
queryFile = open('MajorDepressiveDisorderUseCase.query', 'r').read()

graph = rdflib.Graph()
graph.parse( jsonldFile , format = 'json-ld' )

result = graph.query( queryFile )

symptoms = []
for ( symptom , description ) in result:
    symptoms.append( ( unicode( symptom ) , unicode( description ) ) )

print 'The patient comes to the office reporting',
for ( idS , ( symptom , description ) ) in enumerate( symptoms ):
    print description,
    if idS == len(symptoms) - 1:
        print '.'
    elif idS == len(symptoms) - 2:
        print 'and',
    else: print ',',

print 'The most likely diagnostic is Major Depressive Disorder'

print 'Because it includes symptoms of',
for ( idS , ( symptom , description ) ) in enumerate( symptoms ):
    print symptom,
    if idS == len(symptoms) - 1:
        print '.'
    elif idS == len(symptoms) - 2:
        print 'and',
    else: print ',',

