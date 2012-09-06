# -*- coding: utf-8 -*-

db.describe_table('products',
    Field('brand_id', 'reference brands'),
    Field('unit_id', 'referemce units'),
    Field('vendor_id', 'reference vendors'),
    Field('code', 'string'),
    Field('alternative_code', 'string'),
    Field('part_number', 'string'),
    Field('model', 'string'),
    Field('image', 'upload', uploadfield=True),
    Field('standard_cost', )
)
