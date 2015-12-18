# Semantic automatic generation of clinical case exercises focused on diagnostic criteria

Lucas O. Teixeira  
João Ricardo Vissoci  
Bruno Melo  
Ricardo Pietrobon

## Abstract


<!-- write at the end -->

## Introduction

According to the World Health Organization (WHO), mental illnesses are currently the greatest source of burden across all countries, responsible for a cost of nearly 2.5 trillion dollars in 2010 (@alwan2011global). This figure represents more than the annual GDP of 206 countries (United Nations, 2012). As a result, institutions such as the NIH have set mental health as one of their top four priorities in 2012 (National Institute of Mental Health- NIMH, 2012). One of the foundations currently used in treating mental disorders <!-- standardize as disorders?? --> is the establishment of clear diagnostic criteria, reinforced by the recently released Diagnostic and Statistical Manual for Mental Disorders - Fifth Edition (DSM-V) <!-- ref -->. Resulting from a task force within the American Psychiatric Association, the DSM-V attempts to provide diagnostic guidance and "training materials" (American Psychiatric Association - APA - 2014), ultimately improving the accuracy of diagnoses in clinical practice (APA, 2013). Despite its success in establishing consensus regarding specific criteria, the DSM-V's criteria has limitation in capturing contextual factors that almost invariably accompany mental conditions (Paris, 2013; Gintner, 2014). For example, <!-- contexto sociais -->

<!-- Despite its success in some fronts, the DSM-V does not capture the complexity mental disorders are complex and their management frequently requires a connection between biological basis, personality functioning, medical conditions, relevant stressors and environmental problems. (NIMH, 2012; Gintner,2014). As a result, developing efficient diagnostic skills in this area goes beyond providing stable criteria and requires the development of high quality educational strategies to avoid a narrow approach that would disregard contextual factors (Paris, 2013; Gintner, 2014). To our knowledge, however, such comprehensive educational approaches are rarely available. -->

In other to improve the diagnosis of mental disorders, the American Psychiatric Association (APA) recommends that healthcare professionals should take into account aspects such as "cultural sensitivity" and a "comprehensive and person-centered assessment" (APA, 2013; Gintner,2014). However, in order to create a training environment to achieve these holistic diagnostic skills would require carefully crafted educational material, therefore increasing its cost and reducing scalability (Gierl and Lai, 2013). For example, the cost to develop and single item (question) in some medical exams can reach up to 1500 to 2500 US dollars (Rudner, 2010).

One recent alternative to achieve scalability and mass development of educational exercises is automatic item generation (AIG), defined as the creation of questions (items) using algorithms and automation (Deane, 2003). Among the advantages of AIG are the possibility of quickly delivering exercises in large scale, reducing recall bias, providing prompt feedback, performing quick comparison between subjects and decreasing costs (Gierl et al, 2012). Nonetheless, the applications of AIG are usually limited to simple, non-contextual items, therefore not making it the option of choice for complex or abstract subjects <!-- ref -->. As a consequence, the diagnosis of mental illnesses would be difficult to implement into a vocabulary-fixed database as is typical of AIG (Deane, 2003). As a way to overcome this limitation, researchers in other fields have applied Web Semantics to add context to <!-- example??? + citar-->. Despite the possibility of combining AIG and Web Semantics, to our knowledge no previous research has addressed this possibility.

In face of this gap in the literature, the objective of this article is to develop a framework where semantic web technologies are used to automatically generate highly contextualized exercises (items) in mental health. Specifically, we describe the ontological framework as well as its integration with the widely used Learning Management System [Open edX](http://code.edx.org/). <!-- We will do the integration in this study? -->


## Methods
### Ethics

Since this project does not involve human subjects, the Institutional Review Board of the University of São Paulo deemed it as exempt from review. <!-- ich number -->

<!--
### Source of Diagnostic Guidelines

Since this project did not involve subjects and the data also did not refer to participants, it was considered exempt from review on an Institutional Review Board. 

add dsm v -->


### Source of diagnostic criteria

For this article we used the diagnostic criteria for [major depressive disorder]() <!-- Lucas, please add --> and [schizophrenia](http://ccpweb.wustl.edu/pdfs/2013_defdes.pdf) as established by the [Fifth Edition of the Diagnostic and Statistical Manual of Mental Disorders (DSM-5)](http://www.dsm5.org/Pages/Default.aspx) 


### Ontology engineering methodology

We followed the main principles of [Unified Process for ONtology (UPON)](https://docs.google.com/file/d/0B4Ke-17mTW1_eWZpeUNRa2pUVVE/edit) during the ontology development, with LOT serving as the ontology engineer and RP and GM serving as content experts.

Two healthcare (RP and GM) researchers selected the two <!--four--> documents containing the diagnostic criteria. There was no intention to make these cases to be representative of all conditions. The ontology was then created in conjunction between the ontology engineer (LOT) and the two healthcare researchers. Following the UPON ontology engineering approach, the experts iterated to ensure that the ontology adequately provided an accurate representation of the diagnostic criteria, that its query provided the components necessary to automatically generate itens, and that the two healthcare experts agreed that the items provided an adequate way to assess diagnostic criteria.

<!-- observer agreement -->



### Informal use case

The ontology development was primarily based on the following informal use case:

1. A item (exercise) is developed to represent a typical clinical case exercise (Table 1 and 2).
2. This clinical case exercise is stripped of specific symptoms, signs and diagnoses, which are then replaced by fields to be instantiated by an ontology query, ultimately resulting in an item template.
3. The ontology is then designed so that it can meet two requirements:
    * Queries should result in responses that can be used to instantiate the template
    * The ontology accurately represents the diagnostic criteria

Given that we followed an UPON ontology engineering approach, these three steps were cycled until the ontology reached the status described in this manuscript.

The Table 1 shows a typical item about major depressive disorder. The DSM-5 criteria for major depressive disorder includes nine symptoms: depressed humor, anhedonia, body weight changes, sleep disorders, psychomotor disorders, guiltiness, fatigue, lethargy and suicidal ideation. A patient should have at least four out of the nine symptoms in order to be diagnosed with major depressive disorder, one of them must be depressed humor or anhedonia.

Table 1. Major depressive disorder clinical case exercise

> John, male, 42 years, sought medical aid because he things that something is not right. Says that in recent months is feeling down and tearful. Mentions that he has no desire to do things and everything seems dull. At the start of symptoms the patient thought that it was a healthy related issue: "Doctor, I thought that it was anemia or a thyroid problem, but the exams are all fine". Complains that he has no desire to eat and that his clothes are already getting loose. Reports that he has insomnia, that he wakes in the middle of the night frequently and even taking a drug that his brother gave him he is not sleeping right. States that sometimes he has some 'bad ideas' and even think to end his life but when he remembers his children the thoughts disappear. The patient stays crestfallen most part of the appointment and says that he feels guilty for being 'a burden' on his family.

<!-- Lucas, I will link each description in the item above to the corresponding symptom -->

Table 2. Schizophrenia clinical case exercise

> Mark, male, 21 years, ...

The item in Table 1 and Table 2 can be stripped into: personal information about the patient, symptoms reported, signs noticed by the doctor and laboratory results. Furthermore, personal information can be stripped into name, gender, age and reason for the visit and symptoms can be stripped into mandatory and optional. We have decided to split symptoms into two groups: mandatory and optional. This was done because often the diagnostic criteria of DSM-5 includes a set of symptoms and requires that subset of these to be present. <!-- Lucas, I will explain better -->


### Item model

<!-- gustavo to add clinical case -->

<!-- Ricardo, can I use the same above in the item model below? -->

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

We develop a ontology to represent the clinical case exercises, called [Mental Disorders Automatic Item Generation Ontology]() (MDAIG)<!--Lucas, create purl and describe here -->. The classes and properties present in MDAIG are highly based in the Gierl (2012) work. The MDAIG is represented in Figure 1. 

Figure 1. MDAIG Structure

![Mental Disorders Automatic Item Generation Ontology](https://github.com/rpietro/semantic_exercises/blob/master/mdaig.png)

<!-- Lucas, will improve figure later-->

The following example is the major depressive disorder item model modeled in MDAIG: <!--Lucas, create figure of one item model representation-->

Finally, MDAIG is licensed under [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html) and it is available under our [SPARQL Endpoint]().

#### Classes

Table 1. MDAIG Classes

OWL Class | Description
----------|------------
ItemModel | The ItemModel class represents an item model used to produce different items.
ProblemAndScenario | The ProblemAndScenario class represents the main subject of the item model. It includes a disease, a disorder, a treatment, etc. The problem is a MeSH term. For example, a problem could be major depressive disorder, schizophrenia, etc.
SourceOfInformation | The SourceOfInformation class represents any source of information used by an item model. It includes personal information, physical examination done by the doctor, laboratory results and symptoms.
PersonalInformation | The PersonalInformation class represents any information used to characterize the patient. It includes name, gender, age, reason for the visit and personal thoughts. The FOAF vocabulary is used to characterize patients.
SignAndSymptom | The SignAndSymptom class represents any symptoms reported by the patient or a sign noticed by the doctor. It includes mandatory symptoms and optional symptoms. The signs and symptoms used are MeSH terms. For example, a symptom could be fatigue, anhedonia, depressed humor, delusions, etc.
PhysicalExamination | The PhysicalExamination class represents represents any physical examination done and its result. For example, physical examination could be blood pressure, heart rate, temperature, respiration rate, etc.
LaboratoryResult | The LaboratoryResult class represents represents any laboratory exam done and its result. For example, laboratory results could be blood count, urinalysis, cholesterol level, blood glucose sugar, etc.
MandatorySymptom | The MandatorySymptom class represents a set of symptoms that a patient must have.
OptionalSymptom | The OptionalSymtpom class represents a set of symptoms that a patient may have.

#### Properties

Table 2. MDAIG Properties

OWL Properties | Description
---------------|------------
hasProblemAreaAndAssociateScenarios | The hasProblemAreaAndAssociateScenarios property relates an item model to its main problem. The domain is ItemModel and the range is ProblemAndScenario.
hasPersonalInformation | The hasPersonalInformation property relates an item model to any information used to characterize the patient. The domain is ItemModel and the range is PersonalInformation.
hasPhysicalExamination |The hasPhysicalExamination property relates an item model to any information about the physical examination done by a doctor. The domain is ItemModel and the range is PhysicalExamination.
hasLaboratoryResults |The hasLaboratoryResults property relates an item model to any information about the laboratory tests done on the patient. The domain is ItemModel and the range is LaboratoryResults.
hasMandatorySymptoms |The hasMandatorySymptoms property relates an item model to its mandatory symptoms. The domain is ItemModel and the range is MandatorySymptom.
hasMinimumMandatorySymptoms | The hasMinimumMandatorySymptoms property relates an item model to the minimum number of mandatory symptoms that must be present in a generated item. The domain is ItemModel and the range is an integer.
hasOptionalSymptoms |The hasOptionalSymptoms property relates an item model to its optional symptoms. The domain is ItemModel and the range is OptionalSymptom.
hasMinimumOptionalSymptoms |The hasMinimumMandatorySymptoms property relates an item model to the minimum number of optional symptoms that must be present in a generated item. The domain is ItemModel and the range is an integer.


#### Query, inferences and model instantiation





## Results


### Query results

* libraries
    * rdflib https://pypi.python.org/pypi/rdflib
    * rdflib-jsonld https://pypi.python.org/pypi/rdflib-jsonld

Feedback is composed by the full diagnostic criteria

### Semantic representation of Clinical Practice Guidelines using JSON-LD


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


### Application results


## Discussion

To the best of our knowledge, this is the first description of a semantic automated item generation framework applied to mental health. We have found that semantic models of common mental health conditions can be used to generate a large number of reliable, enriched clinical case items (exercises). 

* quality of mental health training (itens) em relation to context
<!-- check book dsm ricardo mandou http://goo.gl/qTmVbr -->


* Previous literature on automatic  itemgeneration and limitations of the non-semantic approach.
	* Advantages to our approach include the ability to model a larger range of item restrictions, in a way that would be difficult or impossible using traditional automatic item generation techniques. Second, since we can include a progressive number of natural language variations in our models, the number of resulting items is almost limitless. The larger number of items not only substantially reduces the cost of item generation, but also improves the security of the resulting item banks. In other words, if individuals undergoing a given test cannot predict which instance of an item model they will be presented with, then they cannot memorize that item and their response is more likely to represent their current ability.
* Previous use of semantic modeling and differences in relation to our modeling approach


Although our study brings a novel approach to the automatic generation of educational items, it does have limitations. First, we have not validated it against a wider range of clinical areas, which might pose different modeling challenges not anticipated by our current model. As a consequence, future models might not be back compatible. Second, our model currently does not apply to treatment in general, and more specifically to Clinical Practice Guidelines. Clinical Practice Guidelines are an essential part in the translation of the best available evidence to the daily healthcare practice, but their addition imposes a number of additional challenges such as the inclusion of treatment vocabularies as well as the treatment of a "situational interpretation" in treatment choice. For example, a given treatment might be applicable to a young patients whereas it might not on an elderly individual.

Based on the previously stated limitations, future research should focus on the expansion of our model to clinical treatment and the inclusion of a situations as a way to introduce a more nuanced level of detail to our items. Although this is, to our knowledge, the first report of a semantic automatic generation approach to clinical case exercises, we believe that its inclusion into existing learning management systems such as the [Open edX](http://code.edx.org/) platform will bring advantages to both learners and instructors.

## References

<!-- Lucas, let's add them in bibtex format since that's easy to process through Rmarkdown -->

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

@book{gierl2012automatic,
  title={Automatic item generation: Theory and practice},
  author={Gierl, Mark J and Haladyna, Thomas M},
  year={2012},
  publisher={Routledge}
}
