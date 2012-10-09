# -*- coding: utf-8 -*-
db.define_table('vendors',
    Field('name', 'string', notnull=True, unique=True),
    Field('address', 'string'),
    Field('country_id', 'reference countries', default=1),
    Field('locality_id', 'reference localities'),
    Field('municipality_id', 'reference municipalities'),
    Field('state_id', 'reference states'),
    Field('zip_code', 'integer', length=5),
    Field('rfc', 'string', length=13),
    Field('website', 'string'),
    Field('bank', 'string'),
    Field('bank_account_number', 'string'),
    Field('branch', 'string'),
    Field('clabe', 'string', length=18),
    Field('status', 'boolean', default=True),
    Field('date_added', 'datetime', default=request.now),
    Field('date_modified', 'datetime', update=request.now),
    Field('added_by', 'reference auth_user',
      default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
      update=auth.user.id if auth.user else 0), migrate=MIGRATE)

db.define_table('vendor_contact_info',
    Field('vendor_id', 'reference vendors', notnull=True),
    Field('contact_type_id', 'reference contact_types', notnull=True,
        label=T('Tipo')),
    Field('description', 'string', notnull=True), migrate=MIGRATE)

db.define_table('vendor_agents',
    Field('vendor_id', 'reference vendors', notnull=True),
    Field('name', 'string', required=True, notnull=True),
    migrate=MIGRATE)

db.define_table('vendor_agent_contact_info',
    Field('vendor_agent_id', 'reference vendor_agents', notnull=True),
    Field('contact_type_id', 'reference contact_types', notnull=True),
    Field('description', 'string', notnull=True), migrate=MIGRATE)
