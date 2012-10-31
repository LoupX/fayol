# -*- coding: utf-8 -*-

db.define_table('inventory_entries',
    Fied('serie', 'string'),
    Field('folio', 'string'),
    Field('branch_id'),
    Field('warehouse_id'),
    Field('date_added'),
    Field('date_modified'),
    Field('date_receipt'),
    Field('user_added'),
    Field('user_modified'),
    Field('user_receipt'),
    migrate=MIGRATE
)

db.define_table('inventory_entry_descriptions',
    Field('inventory_entry_id', 'reference inventory_entries'),
    Field('product_id', 'reference products'),
    Field('quantity'),
    Field('cost'),
    migrate=MIGRATE
)

db.define_table('product_to_stock',
    Field('warehouse_id'),
    Field('branch_id'),
    Field('product_id'),
    Field('stock'),
    migrate=MIGRATE
)


