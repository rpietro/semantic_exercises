
import rdflib
import random

useCases = [
    ('Major Depressive Disorder', "MajorDepressiveDisorder4x1.query"),
    ('Major Depressive Disorder', "MajorDepressiveDisorder4x2.query"),
    ('Major Depressive Disorder', "MajorDepressiveDisorder5x1.query"),
    ('Schizophrenia', "Schizophrenia1x2.query"),
    ('Schizophrenia', "Schizophrenia2x2.query"),
    ('Schizophrenia', "Schizophrenia3x1.query"),
]

( disease , query ) = random.choice( useCases )

jsonldData = open("ClinicalCaseExerciciesOntologyExpanded.jsonld", 'r').read()
queryData = open(query, 'r').read()

graph = rdflib.Graph()
graph.parse( data = jsonldData , format = 'json-ld' )

result = graph.query( queryData )

symptoms = []
for ( symptom , description ) in result:
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

