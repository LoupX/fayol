# -*- coding: utf-8 -*-

db.define_table('categories',
    Field('image', 'upload', uploadfield=True),
    Field('parent_id', 'integer', length=4),
    Field('sort_order', 'integer', length=4),
    Field('status', 'boolean', default=True),
    Field('date_added', 'datetime', default=request.now),
    Field('date_modified', 'datetime', update=request.now),
    Field('added_by', 'reference auth_user',
	      default=auth.user.id if auth.user else None),
    Field('modified_by', 'reference auth_user',
	  update=auth.user.id if auth.user else None),
    migrate=MIGRATE)

db.define_table('category_descriptions',
    Field('category_id', 'reference categories', notnull=True),
    Field('name', 'string', notnull=True, unique=True),
    Field('description', 'text'),
    Field('meta_description', 'string'),
    Field('meta_keywords', 'string'),
    migrate=MIGRATE)
