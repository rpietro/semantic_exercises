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

### Source of Clinical Practice Guidelines

* [National Guideline Clearinghouse](http://www.guideline.gov/) using guidelines focused on Mental Health
* 3 guidelines:


### Use case


#### Diagnosis

Patient is a {{male}}, {{28}} years old, comes to the {{office}}, {{no family support}}. with symptoms of {{crying often}}, {{not being able to sleep at night}} and {{suicidal thinking}}. The most likely diagnosis is:

( ) {{anxiety}}
(x) {{major depression}}
( ) {{obsessive compulsive disorder}}

[explanation]
The {{diagnostic criteria}} for {{major depression}} according to {{DSM-V}} are symptoms of {{crying often}}, {{not being able to sleep at night}} and {{suicidal thinking}}. Signs might include {{}}. Laboratory results might include {{}}. Imaging results might include {{}}
[explanation]




### Evidence-based facts extraction

* two healthcare researchers
* use of executive summary 
* statement example
* observer agreement

JSON (not in a JSON-LD format)

[
{
    "eb-fact" : "",
    "source" : {
        "reference" : "",
        "hyperlink" : "",
        "publication_date" : ""
        },
        "classification" : {
            "diagnosis_cat" : [""],
            "treatment_cat" : [""],
        }
    }

    ]



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

Feedback is composed by the 

### Semantic encoding of Clinical Practice Guidelines using JSON-LD



## Results

## Discussion