<<<<<<< HEAD
# Semi-automatic generation of clinical case exercises based on diagnostic classifications using semantic representation
=======
# Semantic automatic generation of clinical case exercises focused on diagnostic criteria
>>>>>>> 63487b602ac1dfe3b44e9a50b9e2df60c558fb58

Lucas O. Teixeira  
João Ricardo Vissoci  
Bruno Melo  
Ricardo Pietrobon
Gustavo C. Medeiros

## Abstract


<!-- write at the end -->

## Introduction

Although diagnostic guidelines and classifications such as the DSM-V and the ones released for the diagnosis of rheumatological conditions were designed with the intent of facilitating the day to day activities of clinicians around the globe, they are largely delivered in a format that is informative rather than educational. It is therefore no surprise that adherence to these classifications are poorly followed <!-- ref -->, ultimately decreasing the benefit that would arise from a more accurate diagnosis such as the ability to properly follow the best available evidence. To our knowledge, however, there have been no previous attempts to automatically convert diagnostic guidelines to a format that would be directly applicable to a learning environment.

Although a vast amount of literature has been published on the definition of diagnostic criteria for an array of conditions, very little has been published on methods to enhance the learning of these same criteria by healthcare professionals. And yet, there is a substantial amount of literature demonstrating a large degree of disagreement among authors when it comes to the diagnosis of individual cases ([Williams, 2006](http://onlinelibrary.wiley.com/doi/10.1111/j.1365-2133.1994.tb08531.x/abstract); [Reid, 1988](http://www.sciencedirect.com/science/article/pii/S0046817788803447), [Baldereschi, 1994](http://www.neurology.org/content/44/2/239.short)), which can be interpreted as a lack of healthcare educational resources to better train healthcare professionals.

Although the semantic representation of diagnostic criteria has been explored in a number of publications, the use cases they address are all but homogeneous. For example, some ontologies have aimed at decision support by making diagnoses based on electronic medical records ([Mugzach](http://mis.hevra.haifa.ac.il/~morpeleg/pubs/H35.pdf); [Bertaud-Gounot, 2012](http://informahealthcare.com/doi/abs/10.3109/17538157.2011.590258); [Nixdorg, 2011](http://onlinelibrary.wiley.com/doi/10.1111/j.1365-2842.2011.02247.x/abstract;jsessionid=78DD041A12508901281545F3A2C25E5D.f03t01?deniedAccessCustomisedMessage=&userIsAuthenticated=false)), provide a framework to establish conformance with the Basic Formal Ontology ([Ceusters, 2010](http://www.biomedcentral.com/content/pdf/2041-1480-1-10.pdf); [Ceusters, 2006](http://www.sciencedirect.com/science/article/pii/S157082680600014X)), augment existing ontologies with additional vocabulary ([Samson, 2008](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2655950/)), establish semantic similarity within an existing ontology ([Steichen, 2006](http://www.sciencedirect.com/science/article/pii/S0010482505000776)) or to establish general guidelines for ontology development related to medical diagnosis [Scheuermann, 2009](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3041577/); [Burgun, 2005](http://iospress.metapress.com/content/40jwuthjykf9rrjp/);[Abu-Hanna, 1991](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=79706&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D79706)). Despite all of these models, to our knowledge no previous attempt has been made to model diagnosis so that the ontologies could provide the basis for Automatic Item Generation ([Gierl, 2012](http://www.amazon.com/Automatic-Item-Generation-Theory-Practice-ebook/dp/B00979KH6C/ref=tmm_kin_title_0?_encoding=UTF8&sr=8-1&qid=1410142729))<!-- ref -->, or the ability to generate a very large exercises of exercises based on a model.

<!-- review AIG and then criticize for not being semantic

[Lai, 2009](http://www.psych.umn.edu/psylabs/catcentral/pdf%20files/cat09lai.pdf)
[Embretson, 2006](http://www.sciencedirect.com/science/article/pii/S0169716106260231)
[Gierl, 2008](http://www.taotesting.com/advances-automatic-item-generation-and-demonstration)
[Zhongquan, 2008](http://118.145.16.229:81/Jweb_xlkxjz/EN/abstract/abstract2407.shtml)
[Gierl, 2012](http://www.ualberta.ca/~mgierl/files/published-papers/ijt%20item%20models%202012.pdf)

 -->

     

<!-- We chose to use the JSON-LD format for the semantic representation of Clinical Practice Guidelines because it is a very lightweight format, strongly based on JSON and it is as representative as RDF and OWL. Moreover, we adopted the Dublin Core Metadata Standard with Medical Subject Headings controlled vocabulary [Check the possibility of using MEDDRA] in order to standardized our semantic representation allowing others to use it.  -->

<<<<<<< HEAD
The objective of this article is therefore to present the structure and results of a novel methodology using a semantic representation of diagnostic classifications, which is then semi-automatically deployed to clinical case exercises deployable to the [open edX]() learning management system. The architecture and multiple validation cases are presented.
=======
The objective of this article is therefore to present the structure and results of a novel methodology using a semantic representation of diagnostic criteria, which are then semi-automatically deployed to clinical case exercises deployable to the [open edX](http://code.edx.org/) learning management system. The architecture and four validation cases are presented.
>>>>>>> 63487b602ac1dfe3b44e9a50b9e2df60c558fb58




## Methods
### Ethics

<<<<<<< HEAD
### Source of Diagnostic Guidelines

* DSM-V
* Rheumatological diagnostic criteria released by the American Rheumatological Association
=======
Since this project did not involve subjects and the data also did not refer to participants, it was considered exempt from review on an Institutional Review Board. 

>>>>>>> 63487b602ac1dfe3b44e9a50b9e2df60c558fb58



### Source of diagnostic criteria

For this article we used the diagnostic criteria for [major depression]() <!-- Lucas, please add --> and [schizophrenia](http://ccpweb.wustl.edu/pdfs/2013_defdes.pdf) as established by the [Fifth Edition of the Diagnostic and Statistical Manual of Mental Disorders (DSM-5)](http://www.dsm5.org/Pages/Default.aspx) as well as the criteria for rheumatoid arthritis and [polymyalgia rheumatica](http://www.rheumatology.org/ACR/practice/clinical/classification/jra/FINAL_PMR_Class_Criteria_paper.pdf) as established by the [American College of Rheumatology](http://www.rheumatology.org/Practice/Clinical/Classification/Classification_Criteria_for_Rheumatic_Diseases/).




### Ontology engineering methodology


We followed the main principles of [Unified Process for ONtology (UPON)](https://docs.google.com/file/d/0B4Ke-17mTW1_eWZpeUNRa2pUVVE/edit) during the ontology development, with LOT serving as the ontology engineer and RP and GM serving as content experts for, respectively, the musculoskeletal and mental health fields. 

Two healthcare (RP and GM) researchers selected the four documents containing the diagnostic criteria. There was no intention to make these cases to be representative of all conditions. The ontology was then created in conjunction between the ontology engineer (LOT) and the two healthcare researchers. Following the UPON ontology engineering approach, the experts iterated to ensure that the ontology adequately provided an accurate representation of the diagnostic criteria, that its query provided the components necessary to automatically generate itens, and that the two healthcare experts agreed that the items provided an adequate way to assess diagnostic criteria.

<!-- observer agreement -->



### Informal use case

The ontology development was primarily based on the following informal use case:

1. A template item (exercise) is developed to represent a typical clinical case exercise (Table 1).
2. This clinical case exercise is stripped of specific symptoms, signs and diagnoses, which are then replaced by fields to be instantiated by an ontology query, ultimately resulting in an item template (Table 1).
3. The ontology is then designed so that it can meet two requirements:
    * Queries should result in responses that can be used to instantiate the template
    * The ontology accurately represents the diagnostic criteria

Given that we followed an UPON ontology engineering approach, these three steps were cycled until the ontology reached the status described in this manuscript.

Table 1. Clinical case exercise and corresponding template

> Patient with {{socio-demographic }}

<!-- add one template and one instantiated exercise -->

<<<<<<< HEAD
<!-- add DSM-V criteria for depression and RA criteria-->

=======


>>>>>>> 63487b602ac1dfe3b44e9a50b9e2df60c558fb58

### Item model

Um paciente do sexo {{gender}}, {{age}} anos de idade, estado civil {{marital_status}}, vem ao consultório com as seguintes queixas:

<<<<<<< HEAD
=======
* {{natural_language_symptom}}
* {{natural_language_symptom}}
* {{natural_language_symptom}}
* {{natural_language_symptom}}
* {{natural_language_symptom}}
* {{natural_language_symptom}}

O diagnóstico mais provável é:

(x) {{}}
( ) {{}}
( ) {{}}
( ) {{}}
( ) {{}}

[explanation]
{{natural_language_diagnostic_criteria}}
[explanation]
>>>>>>> 63487b602ac1dfe3b44e9a50b9e2df60c558fb58


### Ontology structure

<!-- Lucas, let's come up with a graphical representation of the ontology in graphviz or something. The JSON-LD serialization can then be represented in a separate file within the github repo.  -->

#### Classes


#### Properties


#### Query, inferences and model instantiation




<<<<<<< HEAD

=======

## Results
### Query results

* libraries
    * rdflib https://pypi.python.org/pypi/rdflib
    * rdflib-jsonld https://pypi.python.org/pypi/rdflib-jsonld

http://dublincore.org/documents/dcq-rdf-xml/

[Use a latex listing to show the ontology below]
{
    "@context":
    {
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "dc": "http://purl.org/dc/elements/1.1/",
        "dcterms": "http://purl.org/dc/terms/",
        "foaf": "http://xmlns.com/foaf/0.1/",
        "ns": "http://diseasesdiagnosis.com/vocab#"
    },
    "@graph": 
    [


        {
            "@id": "ns:C23.550.288",
            "dc:subject": 
            {
                "@id": "dcterms:MESH/C23.550.288",
                "rdf:value": "C23.550.288",
                "rdfs:label": "Disease",
                "@type": "dcterms:MESH"
            }
        },


        {
            "@id": "ns:F03.600.300.375",
            "@type": "ns:C23.550.288",
            "ns:minimumQuantityOfOptionalSymptoms": 4,
            "dc:subject": 
            {
                "@id": "dcterms:MESH/F03.600.300.375",
                "rdf:value": "F03.600.300.375",
                "rdfs:label": "Depressive Disorder, Major",
                "@type": "dcterms:MESH"
            },
            "ns:mandatorySymptoms":
            [
                {
                    "dc:subject": 
                    {
                        "@id": "ns:F01.145.126.350",
                        "rdf:value": "F01.145.126.350",
                        "rdfs:label": "Depression",
                        "@type": "dcterms:MESH"
                    },
                },
                {
                    "dc:subject": 
                    {
                        "@id": "ns:C23.888.592.604.039",
                        "rdf:value": "C23.888.592.604.039",
                        "rdfs:label": "Anhedonia",
                        "@type": "dcterms:MESH"
                    },
                }
            ],
            "ns:optionalSymptoms":
            [
                {
                    "dc:subject": 
                    {
                        "@id": "ns:C23.888.144.243",
                        "rdf:value": "C23.888.144.243",
                        "rdfs:label": "Body Weight Changes",
                        "@type": "dcterms:MESH"
                    }
                },
                {
                    "@id": "ns:C10.886.425.800.800",
                    "dc:subject": 
                    {
                        "@id": "ns:C10.886.425",
                        "rdf:value": "C10.886.425",
                        "rdfs:label": "Dyssomnias",
                        "@type": "dcterms:MESH"
                    }
                },
                {
                    "dc:subject": 
                    {
                        "@id": "ns:C23.888.592.604.882.700",
                        "rdf:value": "C23.888.592.604.882.700",
                        "rdfs:label": "Psychomotor Agitation",
                        "@type": "dcterms:MESH"
                    }
                },
                {
                    "dc:subject": 
                    {
                        "@id": "ns:C23.888.369",
                        "rdf:value": "C23.888.369",
                        "rdfs:label": "Fatigue",
                        "@type": "dcterms:MESH"
                    }
                },
                {
                    "dc:subject": 
                    {
                        "@id": "ns:C23.888.592.604.444",
                        "rdf:value": "C23.888.592.604.444",
                        "rdfs:label": "Lethargy",
                        "@type": "dcterms:MESH"
                    },
                    "descriptions":
                    [
                        "descricao 1",
                        "descricao 2",
                        "descricao 3",
                        ...
                    ]
                },
                {
                    "dc:subject": 
                    {
                        "@id": "ns:F01.145.126.980.875.149",
                        "rdf:value": "F01.145.126.980.875.149",
                        "rdfs:label": "Suicidal Ideation",
                        "@type": "dcterms:MESH"
                    }
                }
            ]
        },
    ]
}
>>>>>>> 63487b602ac1dfe3b44e9a50b9e2df60c558fb58


SPARQL Query:

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX ns: <http://diseasesdiagnosis.com/vocab#>

SELECT ?diseaseName

WHERE
{

    ?patient rdf:type foaf:Person .
    ?patient foaf:name ?patientName .

    ?patient ns:hasSymptom ?optionalSymptom .
    ?optionalSymptom dc:subject ?meshOptionalSymptom .
    ?meshOptionalSymptom rdf:value ?optionalSymptomID .
    ?meshOptionalSymptom rdfs:label ?optionalSymptomName .

    ?disease rdf:type ?diseaseType .
    ?diseaseType dc:subject ?meshDiseaseType .
    ?meshDiseaseType rdf:value "C23.550.288" .
    ?meshDiseaseType rdfs:label "Disease" .

    ?disease dc:subject ?meshDisease .
    ?meshDisease rdfs:label ?diseaseName .

    ?disease ns:minimumQuantityOfOptionalSymptoms ?quantityOfOptionalSymptoms .

    ?disease ns:optionalSymptoms ?optionalSymptom .
    ?optionalSymptom dc:subject ?meshOptionalSymptom .
    ?meshOptionalSymptom rdf:value ?optionalSymptomID .
    ?meshOptionalSymptom rdfs:label ?optionalSymptomName .


    FILTER NOT EXISTS {

<<<<<<< HEAD
Feedback is composed by the full diagnostic criteria

### Semantic representation of Clinical Practice Guidelines using JSON-LD
=======
        ?disease ns:mandatorySymptoms ?mandatorySymptom .
        ?mandatorySymptom dc:subject ?meshMandatorySymptom .
        ?meshMandatorySymptom rdf:value ?mandatorySymptomID .
        ?meshMandatorySymptom rdfs:label ?mandatorySymptomName .

        FILTER NOT EXISTS {
>>>>>>> 63487b602ac1dfe3b44e9a50b9e2df60c558fb58

            ?patient ns:hasSymptom ?mandatorySymptom .
            ?mandatorySymptom dc:subject ?meshMandatorySymptom .
            ?meshMandatorySymptom rdf:value ?mandatorySymptomID .
            ?meshMandatorySymptom rdfs:label ?mandatorySymptomName .

<<<<<<< HEAD
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
=======
        }
    }

}
>>>>>>> 63487b602ac1dfe3b44e9a50b9e2df60c558fb58

GROUP BY ?diseaseName ?quantityOfOptionalSymptoms HAVING ( COUNT(?optionalSymptom) >= ?quantityOfOptionalSymptoms )
ORDER BY COUNT(?optionalSymptom)

### Application results


## Discussion

To the best of our knowledge, this is the first description of a semantic automated item generation framework. We have found that semantic models of common mental health and rheumatologic conditions can be used to generate a large number of reliable clinical case items (exercises). 

* Previous literature on automatic generation and limitations of the non-semantic approach.
	* Advantages to our approach include the ability to model a larger range of item restrictions, in a way that would be difficult or impossible using traditional automatic item generation techniques. Second, since we can include a progressive number of natural language variations in our models, the number of resulting items is almost limitless. The larger number of items not only substantially reduces the cost of item generation, but also improves the security of the resulting item banks. In other words, if individuals undergoing a given test cannot predict which instance of an item model they will be presented with, then they cannot memorize that item and their response is more likely to represent their current ability.
* Previous use of semantic modeling and differences in relation to our modeling approach


Although our study brings a novel approach to the automatic generation of educational items, it does have limitations. First, we have not validated it against a wider range of clinical areas, which might pose different modeling challenges not anticipated by our current model. As a consequence, future models might not be back compatible. Second, our model currently does not apply to treatment in general, and more specifically to Clinical Practice Guidelines. Clinical Practice Guidelines are an essential part in the translation of the best available evidence to the daily healthcare practice, but their addition imposes a number of additional challenges such as the inclusion of treatment vocabularies as well as the treatment of a "situational interpretation" in treatment choice. For example, a given treatment might be applicable to a young patients whereas it might not on an elderly individual.

<<<<<<< HEAD
## Discussion


## References

<!-- Lucas, let's add them in bibtex format since that's easy to process through Rmarkdown -->
=======
Based on the previously stated limitations, future research should focus on the expansion of our model to clinical treatment and the inclusion of a situations as a way to introduce a more nuanced level of detail to our items. Although this is, to our knowledge, the first report of a semantic automatic generation approach to clinical case exercises, we believe that its inclusion into existing learning management systems such as the [Open edX](http://code.edx.org/) platform will bring advantages to both learners and instructors.
>>>>>>> 63487b602ac1dfe3b44e9a50b9e2df60c558fb58
