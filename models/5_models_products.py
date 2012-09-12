# -*- coding: utf-8 -*-

db.describe_table('products',
    Field('brand_id', 'reference brands', required=True, notnull=True, label=T('Marca')),
    Field('unit_id', 'referemce units', required=True, notnull=True, label=T('Unidad')),
    Field('code', 'string', label=T('Código')),
    Field('alternative_code', 'string', label=T('Código alternativo')),
    Field('part_number', 'string', label=T('Número de parte')),
    Field('serial_number', 'string', label=T('Número de serie')),
    Field('model', 'string', label=T('Modelo')),
    Field('image', 'upload', uploadfield=True, label=T('Imagen')),
    Field('standard_cost', 'decimal(10,2)', label=T('Costo estandar')),
    Field('markup', 'decimal(3,2)', label=T('Margen de utilidad')),
    Field('status', 'boolean', label=T('Estado')),
    Field('date_added', 'datetime', default=request.now, writable=False, readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False, readable=False),
    Field('added_by', 'references auth_user', default=auth.user.id),
    Field('modified_by', 'references auth_user', update=auth.user.id)
)

db.describe_table('product_descriptions',
    Field('product_id', 'reference products', required=True, notnull=True),
    Field('name', 'string', required=True, notnull=True, label=T('Nombre')),
    Field('alternative_name', 'string', label=T('Nombre alternativo')),
    Field('description', 'text', label=T('Descripción')),
    Field('meta_description', 'string', label=T('Meta descripción')),
    Field('meta_keywords', 'string', label=T('Palabras clave'))
)

db.describe_table('product_to_vendor',
    Field('product_id', 'reference products'),
    Field('vendor_id', 'reference vendors')
)

db.describe_table('product_to_category',
    Field('product_id', 'reference products'),
    Field('category_id', 'reference category')
)

db.describe_table('product_price_lists',
    Field('product_id', 'reference products', required=True, notnull=True),
    Field('name', 'string', required=True, notnull=True),
    Field('price', 'decimal(10,2)', default=0.00),
    Field('status', 'boolean', default=True),
    Field('date_added', 'datetime', default=request.now, writable=False, readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False, readable=False),
    Field('added_by', 'references auth_user', default=auth.user.id),
    Field('modified_by', 'references auth_user', update=auth.user.id)
)

db.products.date_added.represent = lambda date_added, row: date_added.strftime('%d - %m - %Y')
db.products.date_modified.represent = lambda date_modified, row: date_added.strftime('%d - %m - %Y')
db.product_price_lists.date_added.represent = lambda date_added, row: date_added.strftime('%d - %m - %Y')
db.product_price_lists.date_modified.represent = lambda date_modified, row: date_added.strftime('%d - %m - %Y')
