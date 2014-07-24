# Semi-automatic generation of clinical case exercises based on Clinical Practice Guidelines using semantic representation

Lucas O. Teixeira  
João Ricardo Vissoci  
Bruno Melo  
Ricardo Pietrobon

## Abstract


## Introduction

Although Clinical Practice Guidelines were designed with the intent of disseminating the best available evidence to healthcare professionals, they are delivered in a format that is informative rather than educational. It is therefore no surprise that adherence to clinical practice guidelines have been reported to be poor <!-- ref -->, ultimately decreasing the benefit that would arise from the best available evidence being applied to patients. To our knowledge, however, there have been no previous attempts to automatically convert Clinical Practice Guidelines to a format that would be directly applicable to a learning environment.

* lit review education applied to Clinical Practice Guidelines
* lit review of semantic representation of Clinical Practice Guidelines

The objective of this article is therefore to present the structure and results of a novel methodology using a semantic representation of Clinical Practice Guidelines, which is then semi-automatically deployed to clinical case exercises deployable to the [open edX]() learning management system. The architecture and multiple validation cases are presented.




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
