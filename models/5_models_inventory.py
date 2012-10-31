# -*- coding: utf-8 -*-
"""
db.define_table('concepts',
    Field('name', 'string'),
    migrate=MIGRATE)

db.define_table('inventory_entries',
    Field('branch_id', 'reference branches', default=0),
    Field('warehouse_id', 'reference warehouses', default=0),
    Field('reference', 'string'),
    Field('notes', 'string'),
    Field('concept_id', 'reference concepts', default=0),
    Field('date_added', 'datetime', default=request.now),
    Field('date_modified', 'datetime', default=request.now),
    Field('date_receipt', 'datetime', notnull=True),
    Field('added_by', 'reference auth_user',
        default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
        update=auth.user.id if auth.user else 0),
    Field('received_by', 'reference auth_user', default=0),
    migrate=MIGRATE)

db.define_table('inventory_entry_descriptions',
    Field('inventory_entry_id', 'reference inventory_entries'),
    Field('product_id', 'reference products'),
    Field('quantity', 'decimal(12,2)'),
    Field('cost', 'decimal(12,2)', comment='unitary price'),
    migrate=MIGRATE)

db.define_table('inventory_discounts',
    Field('branch_id', 'reference branches', default=0),
    Field('warehouse_id', 'reference warehouses', default=0),
    Field('reference', 'string'),
    Field('notes', 'string'),
    Field('concept_id', 'reference concepts', default=0),
    Field('date_added', 'datetime', default=request.now),
    Field('date_modified', 'datetime', default=request.now),
    Field('added_by', 'reference auth_user',
        default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
        update=auth.user.id if auth.user else 0),
    migrate=MIGRATE)

db.define_table('inventory_discount_descriptions',
    Field('inventory_discount_id', 'reference inventory_discounts'),
    Field('product_id', 'reference products'),
    Field('quantity', 'decimal(12,2)'),
    migrate=MIGRATE)

db.define_table('inventory_transfers',
    Field('source_branch', 'reference branches', default=0),
    Field('source_warehouse', 'reference warehouses', default=0),
    Field('destination_branch', 'reference branches', default=0),
    Field('desination_warehouse', 'reference warehouses', default=0),
    Field('reference', 'string'),
    Field('notes', 'string'),
    Field('concept_id', 'reference concepts', default=7),
    Field('date_added', 'datetime', default=request.now),
    Field('date_modified', 'datetime', default=request.now),
    Field('date_transfer', 'datetime', notnull=True),
    Field('added_by', 'reference auth_user',
        default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
        update=auth.user.id if auth.user else 0),
    Field('transfered_by', 'reference auth_user', default=0),
    migrate=MIGRATE)

db.define_table('inventory_transfer_descriptions',
    Field('inventory_transfer_id', 'reference inventory_transfers'),
    Field('product_id', 'reference products'),
    Field('quantity', 'decimal(12,2)'),
    migrate=MIGRATE)

db.define_table('product_to_stock',
    Field('warehouse_id', 'reference warehouses'),
    Field('branch_id', 'reference branches'),
    Field('product_id', 'reference products'),
    Field('stock', 'decimal(12,2)'),
    migrate=MIGRATE)

if db(db.concepts).isempty():
    concept = db.concepts
    try:
        concept.insert(name='Entrada de almacen')
        concept.insert(name='Incongruencia con inventario físico (Entrada)')
        concept.insert(name='Merma (Salida)')
        concept.insert(name='Devolución al proveedor (Salida)')
        concept.insert(name='Incongruencia con inventario físico (Salida)')
        concept.insert(name='Salida')
        concept.insert(name='Traspaso')
    except Exception as e:
        db.rollback()
        raise HTTP(503, e)
    else:
        db.commit()
"""
