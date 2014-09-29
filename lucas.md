# Semantic automatic generation of clinical case exercises focused on diagnostic criteria

Lucas O. Teixeira  
João Ricardo Vissoci  
Bruno Melo  
Ricardo Pietrobon

## Abstract


<!-- write at the end -->

## Introduction

According to the World Health Organization (WHO), mental illnesses are currently the greatest source of burden across all countries, responsible for a cost of nearly 2.5 trillion dollars in 2010 (@alwan2011global). This figure represents more than the annual GDP of 206 countries (United Nations, 2012). As a result, institutions such as the NIH have set mental health as one of their top four priorities in 2012 (National Institute of Mental Health- NIMH, 2012). One of the foundations currently used in treating mental disorders <!-- standardize as disorders?? --> is the establishment of clear diagnostic criteria for mental disorders <!-- repeitda-->, reinforced by the recently released Diagnostic and Statistical Manual for Mental Disorders - Fifth Edition (DSM-V) <!-- ref -->. Resulting from a task force within the American Psychiatric Association, the DSM-V attempts to provide diagnostic guidance and "training materials" (American Psychiatric Association - APA - 2014), ultimately improving the accuracy of diagnoses in clinical practice (APA, 2013). Despite its success in establishing consensus regarding specific criteria, the DSM-V's criteria has limitation in capturing contextual factors that almost invariably accompany mental conditions (Paris, 2013; Gintner, 2014). For example, <!-- contexto sociais -->

<!-- Despite its success in some fronts, the DSM-V does not capture the complexity mental disorders are complex and their management frequently requires a connection between biological basis, personality functioning, medical conditions, relevant stressors and environmental problems. (NIMH, 2012; Gintner,2014). As a result, developing efficient diagnostic skills in this area goes beyond providing stable criteria and requires the development of high quality educational strategies to avoid a narrow approach that would disregard contextual factors (Paris, 2013; Gintner, 2014). To our knowledge, however, such comprehensive educational approaches are rarely available. -->

In other to improve the diagnosis of mental disorders, the American Psychiatric Association (APA) recommends that healthcare professionals should take into account aspects such as "cultural sensitivity" and a "comprehensive and person-centered assessment" (APA, 2013; Gintner,2014). However, in order to create a training environment to achieve these holistic diagnostic skills would require carefully crafted educational material, therefore increasing its cost and reducing scalability (Gierl and Lai, 2013). For example, the cost to develop and single item (question) in some medical exams can reach up to 1500 to 2500 US dollars (Rudner, 2010).

One recent alternative to achieve scalability and mass development of educational exercises is automatic item generation (AIG), defined as the creation of questions (items) using algorithms and automation (Deane, 2003). Among the advantages of AIG are the possibility of quickly delivering exercises in large scale, reducing recall bias, providing prompt feedback, performing quick comparison between subjects and decreasing costs (Gierl et al, 2012). Nonetheless, the applications of AIG are usually limited to simple, non-contextual items, therefore not making it the option of choice for complex or abstract subjects <!-- ref -->. As a consequence, the diagnosis of mental illnesses would be difficult to implement into a vocabulary-fixed database as is typical of AIG (Deane, 2003). As a way to overcome this limitation, researchers in other fields have applied Web Semantics to add context to <!-- example??? + citar-->. Despite the possibility of combining AIG and Web Semantics, to our knowledge no previous research has addressed this possibility.

In face of this gap in the literature, the objective of this article is to develop a framework where semantic web technologies are used to automatically generate highly contextualized exercises (items) in mental health. Specifically, we describe the ontological framework as well as its integration with the widely used Learning Management System [Open edX](http://code.edx.org/).




## Methods
### Ethics

Since this project did not involve subjects and the data also did not refer to participants, it was considered exempt from review on an Institutional Review Board. 




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




### Item model

Um paciente do sexo {{gender}}, {{age}} anos de idade, estado civil {{marital_status}}, vem ao consultório com as seguintes queixas:

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


### Ontology structure

<!-- Lucas, let's come up with a graphical representation of the ontology in graphviz or something. The JSON-LD serialization can then be represented in a separate file within the github repo.  -->

#### Classes


#### Properties


#### Query, inferences and model instantiation





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

### Application results


## Discussion

To the best of our knowledge, this is the first description of a semantic automated item generation framework. We have found that semantic models of common mental health and rheumatologic conditions can be used to generate a large number of reliable clinical case items (exercises). 

* Previous literature on automatic generation and limitations of the non-semantic approach.
	* Advantages to our approach include the ability to model a larger range of item restrictions, in a way that would be difficult or impossible using traditional automatic item generation techniques. Second, since we can include a progressive number of natural language variations in our models, the number of resulting items is almost limitless. The larger number of items not only substantially reduces the cost of item generation, but also improves the security of the resulting item banks. In other words, if individuals undergoing a given test cannot predict which instance of an item model they will be presented with, then they cannot memorize that item and their response is more likely to represent their current ability.
* Previous use of semantic modeling and differences in relation to our modeling approach


Although our study brings a novel approach to the automatic generation of educational items, it does have limitations. First, we have not validated it against a wider range of clinical areas, which might pose different modeling challenges not anticipated by our current model. As a consequence, future models might not be back compatible. Second, our model currently does not apply to treatment in general, and more specifically to Clinical Practice Guidelines. Clinical Practice Guidelines are an essential part in the translation of the best available evidence to the daily healthcare practice, but their addition imposes a number of additional challenges such as the inclusion of treatment vocabularies as well as the treatment of a "situational interpretation" in treatment choice. For example, a given treatment might be applicable to a young patients whereas it might not on an elderly individual.

Based on the previously stated limitations, future research should focus on the expansion of our model to clinical treatment and the inclusion of a situations as a way to introduce a more nuanced level of detail to our items. Although this is, to our knowledge, the first report of a semantic automatic generation approach to clinical case exercises, we believe that its inclusion into existing learning management systems such as the [Open edX](http://code.edx.org/) platform will bring advantages to both learners and instructors.


1. World Health Organization. (WHO 2011a). Global status report on non-communicable diseases 2010. Geneva: WHO.
2. United Nations Statistic Division. "Growth Rate of GDP and its breakdown - all countries for all years" Available in unstats.un.org/unsd/snaama/dnllist.asp (Accessed September, 2014).
3. http://www.nimh.nih.gov/about/director/2011/the-global-cost-of-mental-illness.shtml
4. American Psychiatric Association, Diagnostic and Statistical Manual of Mental Disorders (2013) "To the DSM-5 User Community" available in http://www.dsm5.org. Accessed in September, 2014.
5. Paris, Joel. The Intelligent Clinician's Guide to the DSM-5RG. Oxford University Press, 2013.
6. American Psychiatric Association. DSM 5. American Psychiatric Association, 2013.
7. Gintner, Gary G. "DSM-5 conceptual changes: Innovations, limitations and clinical implications." The Professional Counselor 4 (2014): 179-190.
8. Gierl, Mark J., and Hollis Lai. "Evaluating the quality of medical multiple‐choice items created with automated processes." Medical education 47.7 (2013): 726-733.
9. Rudner L. Implementing the graduate management admission test computerised adaptive test. In: van der
Linden WJ, Glas CAW, eds. Elements of Adaptive Testing. New York, NY: Springer 2010;151–65.
10.- Deane, Paul, and Kathleen Sheehan. "Automatic item generation via frame semantics: Natural language generation of math word problems." annual meeting of the National Council on Measurement in Education, Chicago, IL. 2003.


@book{alwan2011global,
  title={Global status report on noncommunicable diseases 2010.},
  author={Alwan, Ala and others},
  year={2011},
  publisher={World Health Organization}
}