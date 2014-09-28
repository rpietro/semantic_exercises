# Semi-automatic generation of clinical case exercises based on diagnostic classifications using semantic representation

Lucas O. Teixeira  
João Ricardo Vissoci  
Bruno Melo  
Ricardo Pietrobon

## Abstract


## Introduction

Although diagnostic guidelines and classifications such as the DSM-V and the ones released for the diagnosis of rheumatological conditions were designed with the intent of facilitating the day to day activities of clinicians around the globe, they are largely delivered in a format that is informative rather than educational. It is therefore no surprise that adherence to these classifications are poorly followed <!-- ref -->, ultimately decreasing the benefit that would arise from a more accurate diagnosis such as the ability to properly follow the best available evidence. To our knowledge, however, there have been no previous attempts to automatically convert diagnostic guidelines to a format that would be directly applicable to a learning environment.

* lit review education applied to Clinical Practice Guidelines
* lit review of semantic representation of Clinical Practice Guidelines

The objective of this article is therefore to present the structure and results of a novel methodology using a semantic representation of diagnostic classifications, which is then semi-automatically deployed to clinical case exercises deployable to the [open edX]() learning management system. The architecture and multiple validation cases are presented.




## Methods

### Source of Diagnostic Guidelines

* DSM-V
* Rheumatological diagnostic criteria released by the American Rheumatological Association


### Use case


#### Diagnosis

<!-- add DSM-V criteria for depression and RA criteria-->



#### Treatment





### Evidence-based facts extraction

* two healthcare researchers
* use of executive summary 
* statement example
* observer agreement





### Item ou exercise structure

In order to create our items (the psychometric term for exercises), we have assumed a fixed structure for its stem, alternative options and feedback structure.

#### Stem

The stem might have three components

* Situational information such as patient socio-demographic and social support characteristics
    * "Patient is a {{male}}, {{26}} years old, coming to the {{Emergency Room}} because of" 
    * Variables
        * "gender" : ["male", "female"]
        *  "age" : ""
        *  "visit_setting" : ["Emergency Room", "office"]
    * Some of the variable might or might not influence the choice of an alternative option. The ones that do not can vary randomly within a certain range
* Patient characteristics that are connected to the decision regarding Clinical Practice Guideline
    * symptoms
    * signs
    * laboratory_results
    * imaging_results
    * response to treatment
* 




#### Alternative options


#### Feedback

Feedback is composed by the full diagnostic criteria

### Semantic representation of Clinical Practice Guidelines using JSON-LD

<!-- idea is to build the ontology from the use case -->

<!-- Lucas, here I would add the following:

a. ontology in json-ld, including the classes for symptoms we are trying to represent with a property connecting them to how these symptoms would be represented in a clinical exercise
b. link each symptom and condition to a class from bioportal
c. build a PLO (Personalized Learning Ontology) namespace which will add missing classes along with properties that will give us the inferences we need


  -->


#### Classes

<!-- connect to other ontologies in the Bioportal -->
<!-- Properties -->

#### Queries


#### Demo app


## Results

## Discussion


## References

<!-- Lucas, let's add them in bibtex format since that's easy to process through Rmarkdown -->