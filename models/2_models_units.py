# -*- coding: utf-8 -*-

db.define_table('units',
    Field('name', 'string', required=True, notnull=True, label=T('Nombre')),
    Field('abbreviation', 'string', required=True, notnull=True,
	  label=T('Abreviación')),
    Field('sort_order', 'integer', label=T('Orden')),
    Field('status', 'boolean', default=True, label=T('Estado')),
    Field('date_added', 'datetime', default=request.now, writable=False,
	  readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False,
	  readable=False),
    Field('added_by', 'references auth_user',
	  default=auth.user.id if auth.user else 0),
    Field('modified_by', 'references auth_user',
	  update=auth.user.id if auth.user else 0),
    format='%(name)s')

db.units.date_added.represent = (lambda date_added, row:
		                     date_added.strftime('%d - %m - %Y'))
db.units.date_modified.represent = (lambda date_modified, row: 
		                        date_added.strftime('%d - %m - %Y'))
