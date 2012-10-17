# -*- coding: utf-8 -*-

db.define_table('products',
    Field('brand_id', 'reference brands', required=True, notnull=True),
    Field('unit_id', 'reference units', required=True, notnull=True),
    Field('code', 'string', required=True, notnull=True, unique=True),
    Field('alternative_code', 'string'),
    Field('location', 'string'),
    Field('part_number', 'string'),
    Field('serial_number', 'string'),
    Field('model', 'string'),
    Field('image', 'upload', uploadfield=True),
    Field('standard_cost', 'decimal(10,2)'),
    Field('markup', 'decimal(3,2)'),
    Field('status', 'boolean'),
    Field('date_added', 'datetime', default=request.now, writable=False,
	  readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False,
	  readable=False),
    Field('added_by', 'reference auth_user',
	  default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
	  update=auth.user.id if auth.user else 0),
    migrate=MIGRATE)

db.define_table('product_descriptions',
    Field('product_id', 'reference products', required=True, notnull=True),
    Field('name', 'string', required=True, notnull=True),
    Field('alternative_name', 'string'),
    Field('description', 'text'),
    Field('meta_description', 'string'),
    Field('meta_keywords', 'string'),
    migrate=MIGRATE)

db.define_table('product_to_vendor',
    Field('product_id', 'reference products'),
    Field('vendor_id', 'reference vendors'),
    migrate=MIGRATE)

db.define_table('product_to_category',
    Field('product_id', 'reference products'),
    Field('category_id', 'reference categories'),
    migrate=MIGRATE)

db.define_table('product_price_lists',
    Field('product_id', 'reference products', required=True, notnull=True),
    Field('name', 'string', required=True, notnull=True),
    Field('price', 'decimal(10,2)', default=0.00),
    Field('is_default', 'boolean', default=False),
    Field('status', 'boolean', default=True),
    Field('date_added', 'datetime', default=request.now),
    Field('date_modified', 'datetime', update=request.now),
    Field('added_by', 'reference auth_user',
	  default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
	  update=auth.user.id if auth.user else 0),
    migrate=MIGRATE)
