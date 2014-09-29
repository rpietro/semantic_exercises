
import rdflib
import random


jsonldData = open('ClinicalCaseExerciciesOntologyExpanded.jsonld', 'r').read()
queryData = open('selectCase.query', 'r').read()

graph = rdflib.Graph()
graph.parse( data = jsonldData , format = 'json-ld' )

case = rdflib.Literal( random.choice( [ u'John' , u'Mark' ] ) )

result = graph.query( queryData )

symptoms = []
for ( disease , symptom , description ) in result:
    symptoms.append( ( str( symptom ) , str( description ) ) )

print ('The patient comes to the office reporting', end=' ')
for ( idS , ( symptom , description ) ) in enumerate( symptoms ):
    print (description,end='')
    if idS == len(symptoms) - 1:
        print ('.')
    elif idS == len(symptoms) - 2:
        print (' and',end=' ')
    else: print (',',end=' ')

print ('The most likely diagnostic is ' + disease)

print ('Because it includes symptoms of',end=' ')
for ( idS , ( symptom , description ) ) in enumerate( symptoms ):
    print (symptom,end='')
    if idS == len(symptoms) - 1:
        print ('.')
    elif idS == len(symptoms) - 2:
        print (' and',end=' ')
    else: print (',',end=' ')
