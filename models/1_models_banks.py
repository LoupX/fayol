# -*- coding: utf-8 -*-

db.define_table('banks',
    Field('abm_number', 'integer', length=3, notnull=True),
    Field('institution_name', 'string', notnull=True),
    Field('short_name', 'string', notnull=True),
    format='%(short_name)s'
)

"""
try:
    db.executesql('CREATE INDEX idx_banks_name ON banks (abm_number, (upper(short_name)));')
except:
    pass
"""
