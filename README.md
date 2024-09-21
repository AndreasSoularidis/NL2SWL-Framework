# NL2SWL-Framework
LLM-assisted generation of SWRL rules from natural language

## What is NL2SWRL
The NL2SWRL is an LLM-based framework for translating rule in natural language (NL) into Semantic Web Rule Language (SWRL).

## Research Methodology
### Utilized (Experimental) Ontology

### Rules in Natural Language following the template-driven approach
⦁	Rule 1: IF Gas Is Recognized At Coordinates AND Fire Is Recognized At Coordinates AND Agents Is Nearby to Coordinates THEN Send Alert to Agents AND Agents Abort Mission.
⦁	Rule 2: IF  Person Is Recognized At Coordinates AND Has Heart Rate less than 30 pulses per minute AND Location in Coordinates Is Safe THEN Send To Coordinates a Search and Rescue Team.
⦁	Rule 3: IF House On Fire Is Recognized At Coordinates AND Person has Voice Sign 'help' THEN Send Alert to Fire Station AND Send To Coordinates a Search and Rescue Team  AND Send To Coordinates a Flying Drone Agent AND Send To Coordinates a Spot Robot Agent

![methodology (1)](https://github.com/user-attachments/assets/4cec711b-afbe-4049-b34b-c2cb3f64f29e)

### Phase 1
In this phase, the framework utilizes all the available components i.e., RAG (ontology concepts) and prompt engineering (list of examples, list of guidelines).
The prompt template is the following:
![phase_1](https://github.com/user-attachments/assets/2eb31369-537c-4779-bae3-2aeb6d1dc6a5)

### Phase 2
In the second phase, the framework utilizes only the RAG component (ontology concepts). The prompt template is the following:
![phase_2](https://github.com/user-attachments/assets/f5105d88-a8fb-4903-b74e-45d2fa077fe1)

### Phase 3
In the third phase, the framework does not use any component.The prompt template is the following:
![phase_3](https://github.com/user-attachments/assets/b9a34553-19ef-4df8-b147-d478a88ac3bb)

### Results
![image](https://github.com/user-attachments/assets/0a6a63dd-2b0f-4ff5-86aa-d7f475b11e45)

For the detailed results see here

### Example
#### Phase 1: Final prompt after the retrieved documents of RAG
```
Act as an ontology engineer. Use the following content (examples, part of the ontology, and common mistakes) as a guide to translate the natural language rule you are given into a SWRL rule. 
EXAMPLES

Example 1
Rule in natural language: IF a Person Has a Sibling who Is a Man, THEN the Person Has a Brother.
SWRL rule: Person(?p) ^ hasSibling(?p, ?s) ^ Person(?s) ^ IsMan(?s) -> hasBrother(?p, ?s)

Example 2
Rule in natural language: IF a Person Has a Phone Number that starts with '+', THEN the Person Has an International Phone Number.
SWRL rule: Person(?p) ^ PhoneNumber(?number) ^ hasPhoneNumber(?p, ?number) ^ swrlb:startsWith(?number, "+") -> hasInternationalPhoneNumber(?p, true)

Example 3
Rule in natural language:  IF a Person Has an Age greater than 17, THEN the Person is an Adult and Has IdCard.
SWRL rule: Person(?p) ^ hasAge(?p, ?age) ^ Age(?age) ^ swrlb:greaterThan(?age, 17) ^ IdCard(?id) -> Adult(?p) ^ hasIdCard(?p, ?id)

Example 4
Rule in natural language:  IF a Publication Has two different Authors, THEN those Authors have Cooperated With each other.
SWRL rule: Publication(?p) ^ Author(?y) ^ Author(?z) ^ hasAuthor(?p, ?y) ^ hasAuthor(?p, ?z) ^ differentFrom(?y, ?z) -> cooperatedWith(?y, ?z)

Example 5
Rule in natural language: IF a Researcher Has Published more than 10 papers in a Top-Tier Conference, THEN the Researcher is a Prominent Researcher and Has a High Citation Impact.
SWRL rule: Researcher(?r) ^ hasPublished(?r, ?p) ^ Conference(?p) ^ topTierConference(?p) ^ swrlb:greaterThan(count(?p), 10) -> ProminentResearcher(?r) ^ hasHighCitationImpact(?r)

END OF EXAMPLES

PART OF ONTOLOGY 
###http://example.org/fire_rescue_ontology#isRecognizedAt :isRecognizedAt rdf:type owl:ObjectProperty ; rdfs:domain :Fire , :Gas , :House ; rdfs:range :Coordinates ; rdfs:comment "Indicates that an entity is recognized at specific coordinates." ; rdfs:label "is Recognized At" .

### http://example.org/fire_rescue_ontology#sendTo
:sendAlert rdf:type owl:ObjectProperty ;

rdfs:domain :Alert ;

rdfs:range :Agent ,

:FireStation ;

rdfs:label "send Alert" .

http://example.org/fire_rescue_ontology#sendTo

:sendTo rdf:type owl:ObjectProperty ;

rdfs:domain :Agent ;

rdfs:range :Coordinates ;

rdfs:label "send To" .
http://example.org/fire_rescue_ontology#Alert

:Alert rdf:type owl:Class ;

rdfs:comment "Alerts for decision

makers and agents" ;

rdfs:label "Alert" .

###  http://example.org/fire_rescue_ontology#Coordinates :Coordinates rdf:type owl:Class ; rdfs:comment "Represents latitude and longitude coordinates." ; rdfs:label "Coordinates" .

###  http://example.org/fire_rescue_ontology#Fire :Fire rdf:type owl:Class ; rdfs:comment "Represents the presence of fire at specific coordinates." ; rdfs:label "Fire" .

###  http://example.org/fire_rescue_ontology#FireStation :FireStation rdf:type owl:Class ; rdfs:comment "Represents a fire station." ; rdfs:label "Fire Station" .

###  http://example.org/fire_rescue_ontology#hasCoordinates :hasCoordinates rdf:type owl:ObjectProperty ; rdfs:domain :Fire , :House , :Location ; rdfs:range :Coordinates ; rdfs:comment "Specifies the coordinates of an entity." ; rdfs:label "has Coordinates" .

###  http://example.org/fire_rescue_ontology#hasParticipants

:hasParticipants rdf:type owl:ObjectProperty ;

rdfs:domain :Mission ;

rdfs:range :Agent ;

rdfs:label "has Participants" .

###  http://example.org/fire_rescue_ontology#isNearby :isNearby rdf:type owl:ObjectProperty ; rdfs:domain :Agent ; rdfs:range :Coordinates ; rdfs:comment "Indicates that an entity is nearby specific coordinates." ; rdfs:label "is Nearby" .

END OF ONTOLOGY

COMMON GUIDELINES

Please try to implement the following guidelines:
1: Variables e.g., (?something) used in Conclusions must be present in Conditions. So create as many variables as needed in Conditions. 
2: Each atom must have exactly one variable if it represents class.
3: Each atom must have exactly two variables if it represents object property.
4: Each concept must be represented by a class and must be present in Conditions.

END OF COMMON GUIDELINES

The rule in natural language is the following: IF Gas Is Recognized At Coordinates AND Fire Is Recognized At Coordinates AND Agents Is Nearby to Coordinates THEN Send Alert to Agents AND Agents Abort Mission.
Give only the final SWRL rule
```

#### Phase 2: Final prompt after the retrieved documents of RAG
```
Act as an ontology engineer. Use the following content (part of the ontology) as a guide to translate the natural language rule you are given into a SWRL rule. 
PART OF ONTOLOGY 

###  http://example.org/fire_rescue_ontology#isRecognizedAt :isRecognizedAt rdf:type owl:ObjectProperty ; rdfs:domain :Fire , :Gas , :House ; rdfs:range :Coordinates ; rdfs:comment "Indicates that an entity is recognized at specific coordinates." ; rdfs:label "is Recognized At" .

###  http://example.org/fire_rescue_ontology#sendAlert

:sendAlert rdf:type owl:ObjectProperty ;

rdfs:domain :Alert ;

rdfs:range :Agent ,

:FireStation ;

rdfs:label "send Alert" .

###  http://example.org/fire_rescue_ontology#sendTo

:sendTo rdf:type owl:ObjectProperty ;

rdfs:domain :Agent ;

rdfs:range :Coordinates ;

rdfs:label "send To" .

###  http://example.org/fire_rescue_ontology#Alert

:Alert rdf:type owl:Class ;

rdfs:comment "Alerts for decision

makers and agents" ;

rdfs:label "Alert" .

###  http://example.org/fire_rescue_ontology#Coordinates :Coordinates rdf:type owl:Class ; rdfs:comment "Represents latitude and longitude coordinates." ; rdfs:label "Coordinates" .

###  http://example.org/fire_rescue_ontology#Fire :Fire rdf:type owl:Class ; rdfs:comment "Represents the presence of fire at specific coordinates." ; rdfs:label "Fire" .

###  http://example.org/fire_rescue_ontology#FireStation :FireStation rdf:type owl:Class ; rdfs:comment "Represents a fire station." ; rdfs:label "Fire Station" .

###  http://example.org/fire_rescue_ontology#hasCoordinates :hasCoordinates rdf:type owl:ObjectProperty ; rdfs:domain :Fire , :House , :Location ; rdfs:range :Coordinates ; rdfs:comment "Specifies the coordinates of an entity." ; rdfs:label "has Coordinates" .

###  http://example.org/fire_rescue_ontology#hasParticipants

:hasParticipants rdf:type owl:ObjectProperty ;

rdfs:domain :Mission ;

rdfs:range :Agent ;

rdfs:label "has Participants" .

###  http://example.org/fire_rescue_ontology#isNearby :isNearby rdf:type owl:ObjectProperty ; rdfs:domain :Agent ; rdfs:range :Coordinates ; rdfs:comment "Indicates that an entity is nearby specific coordinates." ; rdfs:label "is Nearby" .

END OF ONTOLOGY

The rule in natural language is the following: IF Gas Is Recognized At Coordinates AND Fire Is Recognized At Coordinates AND Agents Is Nearby to Coordinates THEN Send Alert to Agents AND Agents Abort Mission.
Give only the final SWRL rule
```
#### Phase 3: Final prompt
```
Act as an ontology engineer. Translate the natural language rule you are given into a SWRL rule.
The rule in natural language is the following: IF Gas Is Recognized At Coordinates AND Fire Is Recognized At Coordinates AND Agents Is Nearby to Coordinates THEN Send Alert to these Agents AND Agents Abort Mission.
Give only the final SWRL rule
  
```

#### Important
Starting October 2nd, 2024, gpt-4o will point to the gpt-4o-2024-08-06 snapshot [Link Text](https://platform.openai.com/docs/models/gpt-4o)


## Guick Install
Python 3.10
For Windows
```bash
py -m venv .venv
```
```bash
.venv\Scripts\activate
```
```bash
py -m pip install -r requirements.txt
```

For Unix/macOS
```bash
python3 -m venv .venv
```
```bash
source .venv/bin/activate
```
```bash
python3 -m pip install -r requirements.txt
```
