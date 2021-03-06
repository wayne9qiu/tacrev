RELATION_DEFS = {
        "org:alternate_names": [('org', 'organization'), ('org', 'alternate_name')],
        "org:city_of_headquarters": [('org', 'organization'), ('loc', 'city')],
        "org:country_of_headquarters": [('org', 'organization'), ('loc', 'country')],
        "org:dissolved": [('org', 'organization'), ('date', 'dissolved')],
        "org:founded": [('org', 'organization'), ('date', 'founded')],
        "org:founded_by": [('org', 'organization'), ('per', 'founder')],
        "org:member_of": [('org', 'member'), ('org', 'organization')],
        "org:members": [('org', 'organization'), ('org', 'member')],
        "org:number_of_employees/members": [('org', 'organization'), ('num', 'num_employees')],
        "org:parents": [('org', 'daughter_company'), ('org', 'parent_company')],
        "org:political/religious_affiliation": [('org', 'organization'), ('misc', 'affiliation')],
        "org:shareholders": [('org', 'organization'), ('org', 'shareholder')],
        "org:stateorprovince_of_headquarters": [('org', 'organization'), ('loc', 'location')],
        "org:subsidiaries": [('org', 'organization'), ('org', 'subsidiary')],
        "org:top_members/employees": [('org', 'organization'), ('per', 'member')],
        "org:website": [('org', 'organization'), ('url', 'website')],
        "per:age": [('per', 'person'), ('num', 'age')],
        "per:alternate_names": [('per', 'person'), ('per', 'alternate_name')],
        "per:cause_of_death": [('per', 'person'), ('misc', 'cause_of_death')],
        "per:charges": [('per', 'person'), ('misc', 'charge')],
        "per:children": [('per', 'parent'), ('per', 'child')],
        "per:cities_of_residence": [('per', 'person'), ('loc', 'city')],
        "per:city_of_birth": [('per', 'person'), ('loc', 'city')],
        "per:city_of_death": [('per', 'person'), ('loc', 'city')],
        "per:countries_of_residence": [('per', 'person'), ('loc', 'country')],
        "per:country_of_birth": [('per', 'person'), ('loc', 'country')],
        "per:country_of_death": [('per', 'person'), ('loc', 'country')],
        "per:date_of_birth": [('per', 'person'), ('date', 'date_of_birth')],
        "per:date_of_death": [('per', 'person'), ('date', 'date_of_death')],
        "per:employee_of": [('per', 'employee'), ('org', 'employer')],
        "per:origin": [('per', 'person'), ('loc', 'origin')],
        "per:other_family": [('per', 'person'), ('per', 'family_member')],
        "per:parents": [('per', 'person'), ('per', 'parent')],
        "per:religion": [('per', 'person'), ('misc', 'religion')],
        "per:schools_attended": [('per', 'person'), ('org', 'school')],
        "per:siblings": [('per', 'person'), ('per', 'person')],
        "per:stateorprovince_of_birth": [('per', 'person'), ('loc', 'location')],
        "per:stateorprovince_of_death": [('per', 'person'), ('loc', 'location')],
        "per:stateorprovinces_of_residence": [('per', 'person'), ('loc', 'location')],
        "per:spouse": [('per', 'spouse'), ('per', 'spouse')],
        "per:title": [('per', 'person'), ('misc', 'title')],
        "no_relation": [('none', 'none'), ('none', 'none')]
}

TACRED_SUBJ_OBJ_TYPES = {'ORGANIZATION':'ORGANIZATION',
                    'DURATION':'DURATION',
                    'PERSON':'PERSON',
                    'TITLE':'TITLE',
                    'NUMBER':'NUMBER',
                    'CITY':'LOCATION',
                    'STATE_OR_PROVINCE':'LOCATION',
                    'RELIGION':'RELIGION',
                    'COUNTRY':'LOCATION',
                    'URL':'URL',
                    'DATE':'DATE',
                    'LOCATION':'LOCATION',
                    'NATIONALITY':'LOCATION',
                    'MISC':'MISC',
                    'CRIMINAL_CHARGE':'CRIMINAL_CHARGE',
                    'IDEOLOGY':'IDEOLOGY',
                    'CAUSE_OF_DEATH':'CAUSE_OF_DEATH'}

INVERSE_RELATIONS = {
    "per:children": "per:parents",
    "per:parents": "per:children",
    "org:member_of": "org:members",
    "org:members": "org:member_of",
    "org:parents": "org:subsidiaries",
    "org:subsidiaries": "org:parents"
}