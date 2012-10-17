# -*- coding: utf-8 -*-

db.define_table('brands',
    Field('image', 'upload', uploadfield=True),
    Field('sort_order', 'integer', length=4),
    Field('status', 'boolean', default=True),
    Field('date_added', 'datetime', default=request.now),
    Field('date_modified', 'datetime', update=request.now),
    Field('added_by', 'reference auth_user',
	  default=auth.user.id if auth.user else None),
    Field('modified_by', 'reference auth_user',
	  update=auth.user.id if auth.user else None),
    migrate=MIGRATE)

db.define_table('brand_descriptions',
    Field('brand_id', 'reference brands', notnull=True),
    Field('name', 'string', unique=True, notnull=True),
    Field('description', 'text'),
    Field('meta_description', 'string'),
    Field('meta_keywords', 'string'),
    migrate=MIGRATE)
