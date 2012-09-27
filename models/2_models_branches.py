# -*- coding: utf-8 -*-
db.define_table('company_addresses',
    Field('address', 'string', notnull=True),
    Field('suburb', 'string', comment='colonia', notnull=True),
    Field('country_id', 'references countries', notnull=True),
    Field('state_id', 'references states', notnull=True),
    Field('municipality_id', 'references municipalities', notnull=True),
    Field('locality_id', 'references localities', notnull=True),
    Field('zip_code', 'integer', length=5))

db.define_table('company_tax_info',
    Field('business_name', 'string', comment='razón social'),
    Field('tax', 'string', comment='régimen fiscal'))

db.define_table('branches',
    Field('name', 'string', notnull=True, unique=True),
    Field('address_id', 'references addresses'),
    Field('tax_information_id', 'references tax_information'))

db.define_table('warehouse',
    Field('name', 'string', notnull=True, unique=True),
    Field('address_id', 'references addresses'))

