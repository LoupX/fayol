# -*- coding: utf-8 -*-
db.define_table('company_addresses',
    Field('address', 'string', notnull=True),
    Field('suburb', 'string', comment='colonia', notnull=True),
    Field('country_id', 'reference countries', default=1),
    Field('state_id', 'reference states', notnull=True),
    Field('municipality_id', 'reference municipalities', notnull=True),
    Field('locality_id', 'reference localities', notnull=True),
    Field('zip_code', 'string', length=5),
    Field('status', 'boolean', default=True),
    Field('date_added', 'datetime', default=request.now),
    Field('date_modified', 'datetime', update=request.now),
    Field('added_by', 'reference auth_user',
      default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
      update=auth.user.id if auth.user else 0),
    migrate=MIGRATE)

db.define_table('company_tax_info',
    Field('business_name', 'string', comment='razón social'),
    Field('rfc', 'string', length='13', unique=True),
    Field('tax', 'string', comment='régimen fiscal'),
    Field('status', 'boolean', default=True),
    Field('date_added', 'datetime', default=request.now),
    Field('date_modified', 'datetime', update=request.now),
    Field('added_by', 'reference auth_user',
      default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
      update=auth.user.id if auth.user else 0),
    migrate=MIGRATE)

db.define_table('branches',
    Field('name', 'string', notnull=True, unique=True),
    Field('company_address_id', 'reference company_addresses', required=True),
    Field('company_tax_info_id', 'reference company_tax_info'),
    Field('status', 'boolean', default=True),
    Field('date_added', 'datetime', default=request.now),
    Field('date_modified', 'datetime', update=request.now),
    Field('added_by', 'reference auth_user',
      default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
      update=auth.user.id if auth.user else 0),
    migrate=MIGRATE)

db.define_table('warehouses',
    Field('name', 'string', notnull=True, unique=True),
    Field('company_address_id', 'reference company_addresses'),
    Field('status', 'boolean', default=True, label=T('Estado')),
    Field('date_added', 'datetime', default=request.now, writable=False,
      readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False,
      readable=False),
    Field('added_by', 'reference auth_user',
      default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
      update=auth.user.id if auth.user else 0), migrate=MIGRATE)
