# -*- coding: utf-8 -*-

db.define_table('vendors',
    Field('name', 'string', required=True, notnull=True, label=T('Nombre')),
    Field('address', 'string', label=T('Dirección')),
    Field('city', 'string', label=T('Ciudad')),
    Field('municipality', 'string', label=T('Municipio')),
    Field('state', 'string', label=T('Estado')),
    Field('zip_code', 'integer', length=5, label=T('Código postal')),
    Field('rfc', 'string', length=13, label='RFC'),
    Field('website', 'string', label=T('Sitio web')),
    Field('bank', 'string', label=T('Banco')),
    Field('bank_account_number', 'integer', label=T('Número de cuenta')),
    Field('branch', 'string', label=T('Sucursal')),
    Field('clabe', 'integer', length=18, label='CLABE'),
    Field('date_added', 'datetime', default=request.now, writable=False, readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False, readable=False),
    Field('added_by', 'references auth_user', default=auth.user.id if auth.user else 0),
    Field('modified_by', 'references auth_user', update=auth.user.id if auth.user else 0),
    format='%(name)s'
)

db.define_table('vendor_contact_info',
    Field('vendor_id', 'reference vendors'),
    Field('type', 'string', label=T('Tipo')),
    Field('description', 'string', label=T('Descripción')) #It could be email address, phone number or any other contact information.
)

db.define_table('vendor_agents',
    Field('vendor_id', 'reference vendors'),
    Field('name', 'string', label=T('nombres')),
    Field('last_name', 'string', label=T('Apellidos')),
    Field('date_added', 'datetime', default=request.now, writable=False, readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False, readable=False),
    Field('added_by', 'references auth_user', default=auth.user.id if auth.user else 0),
    Field('modified_by', 'references auth_user', update=auth.user.id if auth.user else 0),
    format='%(name)s %(last_name)s'
)

db.define_table('vendor_agent_contact_info',
    Field('vendor_agent_id', 'reference vendor_agents'),
    Field('type', 'string', label=T('Tipo')),
    Field('description', 'string', label=T('descripción'))
)

"""
try:
    db.executesql('CREATE INDEX idx_vendors_name ON vendors ((upper(name)));', fetch=False)
    db.executesql('CREATE INDEX idx_vendor_agents_name ON vendors ((upper(name)), (upper(last_name)));', fetch=False)
except :
    pass
"""
db.vendors.date_added.represent = lambda date_added, row: date_added.strftime('%d - %m - %Y')
db.vendors.date_modified.represent = lambda date_modified, row: date_added.strftime('%d - %m - %Y')
db.vendor_agents.date_added.represent = lambda date_added, row: date_added.strftime('%d - %m - %Y')
db.vendor_agents.date_modified.represent = lambda date_modified, row: date_added.strftime('%d - %m - %Y')
