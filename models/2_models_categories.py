# -*- coding: utf-8 -*-

db.define_table('categories',
    Field('image', 'upload', uploadfield=True, label=T('Imagen')),
    Field('parent_id', 'integer', length=4, label=T('Categoría padre')),
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

db.define_table('category_descriptions',
    Field('category_id', 'reference categories', required=True, notnull=True,
	  readable=False, writable=False),
    Field('name', 'string', required=True, notnull=True, label=T('Nombre')),
    Field('description', label=T('Descripción')),
    Field('meta_description', label=T('Meta descripción')),
    Field('meta_keywords', label=T('Palabras clave'))
)

db.categories.date_added.represent = (lambda date_added, row: 
		                          date_added.strftime('%d - %m - %Y'))
db.categories.date_modified.represent = (lambda date_modified, row: 
		                             date_added.strftime('%d - %m - %Y'))
