def generate_entity(class_name, name):
    name = name.replace(' ', '_')
    return \
f"""    <Declaration>
        <NamedIndividual IRI="#{name}"/>
    </Declaration>
    <ClassAssertion>
        <Class IRI="#{class_name}"/>
        <NamedIndividual IRI="#{name}"/>
    </ClassAssertion>
"""

def generate_object_property(prop_name, ob1, ob2):
    return f'''    <ObjectPropertyAssertion>
        <ObjectProperty IRI="#{prop_name}"/>
        <NamedIndividual IRI="#{ob2}"/>
        <NamedIndividual IRI="#{ob1}"/>
    </ObjectPropertyAssertion>'''


def generate_data_property(entity_name, value, prop_name, type='string'):
    entity_name = entity_name.replace(' ', '_')
    return f'''    <DataPropertyAssertion>
        <DataProperty IRI="#{prop_name}"/>
        <NamedIndividual IRI="#{entity_name}"/>
        <Literal datatypeIRI="http://www.w3.org/2001/XMLSchema#{type}">{value}</Literal>
    </DataPropertyAssertion>'''
