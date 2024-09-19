class CustomPromptTemplates:

  RAG_template = """
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

    {context}

    END OF ONTOLOGY

    COMMON GUIDELINES

    Please try to implement the following guidelines:
    1: Variables e.g., (?something) used in Conclusions must be present in Conditions. So create as many variables as needed in Conditions. 
    2: Each atom must have exactly one variable if it represents class.
    3: Each atom must have exactly two variables if it represents object property.
    4: Each concept must be represented by a class and must be present in Conditions.

    END OF COMMON GUIDELINES

    The rule in natural language is the following: {question}
    Give only the final SWRL rule
  """

  ontology_template = """
  Act as an ontology engineer. Use the following content (part of the ontology) as a guide to translate the natural language rule you are given into a SWRL rule. 
    PART OF ONTOLOGY 

    {context}

    END OF ONTOLOGY

    The rule in natural language is the following: {question}
    Give only the final SWRL rule
  """
  

  simple_template = """  Act as an ontology engineer. Translate the natural language rule you are given into a SWRL rule.
    The rule in natural language is the following: {question}
    Give only the final SWRL rule
  """
  
  
  @staticmethod
  def rules():
    rule_1 = """IF Gas Is Recognized At Coordinates AND Fire Is Recognized At Coordinates AND Agents Is Nearby to Coordinates THEN Send Alert to Agents AND Agents Abort Mission."""
    rule_2 = """IF a Person Is Recognized At Coordinates AND Has Heart Rate less than 30 pulses per minute AND the Location in Coordinates Is Safe THEN Send To coordinates a Search and Rescue Team."""
    rule_3 = """IF House On Fire Is Recognized At Coordinates AND Person has Voice Sign 'help' THEN Send Alert to the Fire Station AND Send To coordinates a Search and Rescue Team  AND Send To coordinates a Flying Drone Agent AND Send To coordinates a Spot Robot Agent."""

    return [rule_1, rule_2, rule_3]
