# -*- coding: utf-8 -*-

db.define_table('units',
    Field('name', 'string', notnull=True),
    Field('abbreviation', 'string', notnull=True),
    Field('sort_order', 'integer', label=T('Orden')),
    Field('status', 'boolean', default=True, label=T('Estado')),
    Field('date_added', 'datetime', default=request.now, writable=False,
	  readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False,
	  readable=False),
    Field('added_by', 'reference auth_user',
	  default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
	  update=auth.user.id if auth.user else 0),
    format='%(name)s', migrate=MIGRATE)
