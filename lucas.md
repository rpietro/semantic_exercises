# Semi-automatic generation of clinical case exercises based on Clinical Practice Guidelines using semantic representation

Lucas O. Teixeira
João Ricardo Vissoci  
Bruno Melo  
Ricardo Pietrobon

## Abstract


## Introduction

Although Clinical Practice Guidelines were designed with the intent of disseminating the best available evidence to healthcare professionals

 the widespread use of electronic medical records around the world, an unprecedented opportunity is presented to connect the best available evidence at the point of care. This opportunity is not without challenges, however, some of the most important ones being represented by most electronic medical records being based on free text rather than discrete fields, as well as the lack of semantic connection between the text categories and the corresponding Clinical Practice Guidelines. To our knowledge these two challenges have not been addressed up to this point.

* lit review NLP applied to concept discovery in electronic medical records
* lit review of semantic representation of Clinical Practice Guidelines

The objective of this article is therefore to present the structure and results of a novel methodology using natural language processing to abstract concepts from a psychiatric electronic medical record, and then connecting them to the content of Clinical Practice Guidelines focused on Mental Health semantically encoded as [JSON-LD](http://www.w3.org/TR/json-ld/), thus providing a decision-suport framework. The architecture and multiple validation cases are presented.




## Methods

## Electronic medical record data

* describe data
* sample of something like 1000 records

## Natural language processing applied to electronic medical record data

* Concept extraction related to diagnosis, signs and symptoms 

## Semantic encoding of Clinical Practice Guidelines using JSON-LD
* executive summaries of 10 selected Clinical Practice Guidelines encoded as JSON-LD by trained healthcare professionals
* most common conditions selected

## Golden standard dataset connecting raw electronic medical record data to full-text Clinical Practice Guidelines

* two healthcare professionals connecting a sample of 100 patient record data to the respective Clinical Practice Guidelines
* observer agreement data

## Random forest algorithms predicting which medical records should be connected to which Clinical Practice Guidelines

* start with simple algorithms simply connecting diagnoses with Clinical Practice Guidelines
* evolve into further granularity where additional information from medical records allow for connection to more specific sections of each Clinical Practice Guideline
