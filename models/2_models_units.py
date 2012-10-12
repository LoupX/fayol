# -*- coding: utf-8 -*-

db.define_table('units',
    Field('name', 'string', unique=True, notnull=True),
    Field('abbreviation', 'string', unique=True, notnull=True),
    Field('sort_order', 'integer'),
    Field('status', 'boolean', default=True),
    Field('date_added', 'datetime', default=request.now),
    Field('date_modified', 'datetime', update=request.now),
    Field('added_by', 'reference auth_user',
	  default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
	  update=auth.user.id if auth.user else 0),
    migrate=MIGRATE)
