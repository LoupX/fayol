# -*- coding: utf-8 -*-

db.define_table('packages',
    Field('code', 'string', unique=True),
    Field('alternative_code', 'string'),
    Field('image', 'upload', uploadfield=True),
    Field('standard_cost', 'decimal(12,2)'),
    Field('markup', 'decimal(5,2)'),
    Field('status', 'boolean', default=True),
    Field('date_added', 'datetime', default=request.now, writable=False,
        readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False,
        readable=False),
    Field('added_by', 'reference auth_user',
        default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
        update=auth.user.id if auth.user else 0),
    migrate=MIGRATE)

db.define_table('package_to_product',
    Field('package_id', 'reference packages'),
    Field('product_id', 'reference products'),
    migrate=MIGRATE)

db.define_table('package_descriptions',
    Field('package_id', 'reference packages', notnull=True),
    Field('name', 'string', notnull=True),
    Field('description', 'text'),
    migrate=MIGRATE)

db.define_table('package_price_lists',
    Field('package_id', 'reference packages', notnull=True),
    Field('name', 'string', required=True, notnull=True),
    Field('price', 'decimal(12,2)', default=0.00),
    Field('is_default', 'boolean', default=False),
    Field('status', 'boolean', default=True),
    Field('date_added', 'datetime', default=request.now),
    Field('date_modified', 'datetime', update=request.now),
    Field('added_by', 'reference auth_user',
        default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
        update=auth.user.id if auth.user else 0),
    migrate=MIGRATE)
