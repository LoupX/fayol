# -*- coding: utf-8 -*-

db.define_table('clients',
    Field('first_name', 'string', notnull=True),
    Field('last_name', 'string', notnull=True),
    Field('phone', 'string', length=10),
    Field('mobile', 'string', length=10),
    Field('country_id', 'reference countries', default=1),
    Field('state_id', 'reference states'),
    Field('municipality_id', 'reference municipalities'),
    Field('locality_id', 'reference localities'),
    Field('address', 'string'),
    Field('suburb', 'string'),
    Field('zip_code', 'string', length=5),
    Field('rfc', 'string', length=13, notnull=True, unique=True),
    migrate=MIGRATE)
