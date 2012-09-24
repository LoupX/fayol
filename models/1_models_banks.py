# -*- coding: utf-8 -*-

db.define_table('banks',
    Field('abm_number', 'string', length=3, notnull=True),
    Field('institution_name', 'string', notnull=True),
    Field('short_name', 'string', notnull=True),
    format='%(short_name)s'
)
