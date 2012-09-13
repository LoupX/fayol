# -*- coding: utf-8 -*-

db.define_table('states',
    Field('name'),
    Field('hasc', length=5),
    Field('iso', length=3),
    Field('fips', length=4),
    Field('abbreviation', length=5),
    Field('inegi', length=2)
)

db.define_table('municipalities',
    Field('state_id', 'reference states'),
    Field('name'),
    Field('inegi', length=3)
)

db.define_table('localities',
    Field('municipality_id', 'reference municipalities'),
    Field('name'),
    Field('inegi', length=4)
)






