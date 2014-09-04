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

We chose to use the JSON-LD format for the semantic representation of Clinical Practice Guidelines because it is a very lightweight format, strongly based on JSON and it is as representative as RDF and OWL. Moreover, we adopted the Dublin Core Metadata Standard with Medical Subject Headings controlled vocabulary [Check the possibility of using MEDDRA] in order to standardized our semantic representation allowing others to use it. 

The objective of this article is therefore to present the structure and results of a novel methodology using a semantic representation of Clinical Practice Guidelines [Explicitar que vamos trabalhar em apenas alguns casos de uso nessa primeira etapa?], which is then semi-automatically deployed to clinical case exercises deployable to the [open edX]() learning management system. The architecture and multiple validation cases are presented.




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


#### Treatment

Patient is a {{female}}, {{34}} years old, comes to the {{office}}. She presents {{good family support}}. A diagnosis of mild depression is established. The least agreessive treatment and yet recognized as being effective in multiple Clinical Practice Guidelines is:

( ) {{ECT}}
(x) {{isolated psychotherapy}}
( ) {{psychotherapy and tricyclic antidepressants}}

[explanation]
Mild and moderate depression have been demonstrated to be effectively treated with isolated psychotherapy
[explanation]


#### Semantic Representation Design

[A small paragraph explaining JSON-LD, Dublin Core and MeSH and the reason that we used it]

First of all, it is important to state that the ontology was developed primarily to satisfy the use cases described above and that no future requirement was taken into account. The previous assumption allowed our ontology to be very simple and still achieved its objective.

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

Feedback is composed by the full evidence-based fact

### Semantic encoding of Clinical Practice Guidelines using JSON-LD

<!-- idea is to build the ontology from the use case -->




## Results

## Discussion