
import rdflib
import random

useCases = [
        ( 'Major Depressive Disorder', 'MajorDepressiveDisorder.query', (4,6), (1,2) ),
        ( 'Schizophrenia', 'Schizophrenia.query', (1,2), (1,3) )
    ]

( disease, queryFile, (minOptionalSymptoms, maxOptionalSymptoms), (minMandatorySymptoms, maxMandatorySymptoms)  ) = random.choice( useCases )

jsonldData = open("ClinicalCaseExerciciesOntologyExpanded.jsonld", 'r').read()
queryData = open(queryFile, 'r').read()

graph = rdflib.Graph()
graph.parse( data = jsonldData , format = 'json-ld' )

queryData = queryData.replace( '<!-numOfOptionalSymptoms-!>' , str( random.randint( minOptionalSymptoms, maxOptionalSymptoms ) ) )
queryData = queryData.replace( '<!-numOfMandatorySymptoms-!>' , str( random.randint( minMandatorySymptoms, maxMandatorySymptoms ) ) )

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

