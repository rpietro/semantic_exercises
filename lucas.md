# Semi-automatic generation of clinical case exercises based on Clinical Practice Guidelines using semantic representation

Lucas O. Teixeira  
João Ricardo Vissoci  
Bruno Melo  
Ricardo Pietrobon

## Abstract


<!-- write at the end -->

## Introduction

Although Clinical Practice Guidelines were designed with the intent of disseminating the best available evidence to healthcare professionals, they are delivered in a format that is informative rather than educational. It is therefore no surprise that adherence to clinical practice guidelines have been reported to be poor <!-- ref -->, ultimately decreasing the benefit that would arise from the best available evidence being applied to patients. To our knowledge, however, there have been no previous attempts to automatically convert Clinical Practice Guidelines to a format that would be directly applicable to a learning environment.

Although a vast amount of literature has been published on the definition of diagnostic criteria for an array of conditions, very little has been published on methods to enhance the learning of these same criteria by healthcare professionals. And yet, there is a substantial amount of literature demonstrating a large degree of disagreement among authors when it comes to the diagnosis of individual cases ([Williams, 2006](http://onlinelibrary.wiley.com/doi/10.1111/j.1365-2133.1994.tb08531.x/abstract); [Reid, 1988](http://www.sciencedirect.com/science/article/pii/S0046817788803447), [Baldereschi, 1994](http://www.neurology.org/content/44/2/239.short)), which can be interpreted as a lack of healthcare educational resources to better train healthcare professionals.

Although the semantic representation of diagnostic criteria has been explored in a number of publications, the use cases they address are all but homogeneous. For example, some ontologies have aimed at decision support by making diagnoses based on electronic medical records ([Mugzach](http://mis.hevra.haifa.ac.il/~morpeleg/pubs/H35.pdf); [Bertaud-Gounot, 2012](http://informahealthcare.com/doi/abs/10.3109/17538157.2011.590258); [Nixdorg, 2011](http://onlinelibrary.wiley.com/doi/10.1111/j.1365-2842.2011.02247.x/abstract;jsessionid=78DD041A12508901281545F3A2C25E5D.f03t01?deniedAccessCustomisedMessage=&userIsAuthenticated=false)), provide a framework to establish conformance with the Basic Formal Ontology ([Ceusters, 2010](http://www.biomedcentral.com/content/pdf/2041-1480-1-10.pdf)), augment existing ontologies with additional vocabulary ([Samson, 2008](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2655950/)), establish semantic similarity within an existing ontology [(Steichen, 2006)](http://www.sciencedirect.com/science/article/pii/S0010482505000776), establish general guidelines for ontology development in diagnosis [(Scheuermann, 2009)](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3041577/)
    * [](http://iospress.metapress.com/content/40jwuthjykf9rrjp/)
    * [](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=79706&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D79706)
    * [](http://www.sciencedirect.com/science/article/pii/S157082680600014X)

We chose to use the JSON-LD format for the semantic representation of Clinical Practice Guidelines because it is a very lightweight format, strongly based on JSON and it is as representative as RDF and OWL. Moreover, we adopted the Dublin Core Metadata Standard with Medical Subject Headings controlled vocabulary [Check the possibility of using MEDDRA] in order to standardized our semantic representation allowing others to use it. 

The objective of this article is therefore to present the structure and results of a novel methodology using a semantic representation of diagnostic criteria, which are then semi-automatically deployed to clinical case exercises deployable to the [open edX](http://code.edx.org/) learning management system. The architecture and four validation cases are presented.




## Methods


### Ethics

Since this project did not involve subjects and the data also did not refer to participants, it was considered exempt from review on an Institutional Review Board. 

### Source of diagnostic criteria

For this article we used the diagnostic criteria for [major depression]() <!-- Lucas, please add --> and [schizophrenia](http://ccpweb.wustl.edu/pdfs/2013_defdes.pdf) as established by the [Fifth Edition of the Diagnostic and Statistical Manual of Mental Disorders (DSM-5)](http://www.dsm5.org/Pages/Default.aspx) as well as the criteria for rheumatoid arthritis and [polymyalgia rheumatica](http://www.rheumatology.org/ACR/practice/clinical/classification/jra/FINAL_PMR_Class_Criteria_paper.pdf) as established by the [American College of Rheumatology](http://www.rheumatology.org/Practice/Clinical/Classification/Classification_Criteria_for_Rheumatic_Diseases/).

### Ontology engineering methodology


We followed the main principles of [Unified Process for ONtology (UPON)](https://docs.google.com/file/d/0B4Ke-17mTW1_eWZpeUNRa2pUVVE/edit) during the ontology development, with LOT serving as the ontology engineer and RP and GM serving as content experts for, respectively, the musculoskeletal and mental health fields. 


### Informal use case

The ontology development was primarily based on the following informal use case:

1. A template item (exercise) is developed to represent a typical clinical case exercise (Table 1).
2. This clinical case exercise is stripped of specific symptoms, signs and diagnoses, which are then replaced by fields to be instantiated by an ontology query, ultimately resulting in an item template (Table 1).
3. The ontology is then designed so that it can meet two requirements:
    * Queries should result in responses that can be used to instantiate the template
    * The ontology accurately represents the diagnostic criteria

Given that we followed an UPON ontology engineering methodology, these three steps were cycled until the ontology reached the status described in this manuscript.

Table 1. Clinical case exercise and corresponding template

> Patient with {{socio-demographic }}

<!-- add one template and one instantiated exercise -->

#### Semantic Representation Design

[A small paragraph explaining JSON-LD, Dublin Core and MeSH and the reason that we used it]

First of all, it is important to state that the ontology was developed primarily to satisfy the use cases described above and that no future requirement was taken into account. The previous assumption allowed our ontology to be very simple and still achieved its objective.



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

Feedback is composed by the full evidence-based fact

### Semantic encoding of Clinical Practice Guidelines using JSON-LD

<!-- idea is to build the ontology from the use case -->




## Results



### Ontology structure
<!-- Lucas, let's come up with a graphical representation of the ontology in graphviz or something. The JSON-LD serialization can then be represented in a separate file within the github repo.  -->

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


### Querying and inference

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

        ?disease ns:mandatorySymptoms ?mandatorySymptom .
        ?mandatorySymptom dc:subject ?meshMandatorySymptom .
        ?meshMandatorySymptom rdf:value ?mandatorySymptomID .
        ?meshMandatorySymptom rdfs:label ?mandatorySymptomName .

        FILTER NOT EXISTS {

            ?patient ns:hasSymptom ?mandatorySymptom .
            ?mandatorySymptom dc:subject ?meshMandatorySymptom .
            ?meshMandatorySymptom rdf:value ?mandatorySymptomID .
            ?meshMandatorySymptom rdfs:label ?mandatorySymptomName .

        }
    }

}

GROUP BY ?diseaseName ?quantityOfOptionalSymptoms HAVING ( COUNT(?optionalSymptom) >= ?quantityOfOptionalSymptoms )
ORDER BY COUNT(?optionalSymptom)

### Template instantiation

<!-- Lucas what would you suggest as the simplest possible form of an app for this? a CLI? -->

## Discussion