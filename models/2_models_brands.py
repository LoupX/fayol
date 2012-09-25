# -*- coding: utf-8 -*-

db.define_table('brands',
    Field('image', 'upload', required=True, notnull=True, uploadfield=True,
	  label=T('Imagen')),
    Field('sort_order', 'integer', length=4, label=T('Orden')),
    Field('status', 'boolean', default=True, label=T('Estado')),
    Field('date_added', 'datetime', default=request.now, writable=False,
	  readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False,
	  readable=False),
    Field('added_by', 'references auth_user', 
	  default=auth.user.id if auth.user else None),
    Field('modified_by', 'references auth_user', 
	  update=auth.user.id if auth.user else None))

db.define_table('brand_descriptions',
    Field('brand_id', 'reference brands', required=True, notnull=True,
	  readable=False, writable=False),
    Field('name', 'string', required=True, notnull=True, label=T('Nombre')),
    Field('description', label=T('Descripción')),
    Field('meta_description', readable=False, writable=False,
	  label=T('Meta descripción')),
    Field('meta_keywords', readable=False, writable=False,
	  label=T('Palabras clave')))

db.brand_descriptions.format = '%(name)s'
db.brands.date_added.represent = (lambda date_added, row:
	                             date_added.strftime('%d - %m - %Y'))
db.brands.date_modified.represent = (lambda date_modified, row: 
	                                date_added.strftime('%d - %m - %Y'))
