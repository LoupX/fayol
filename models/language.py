# -*- coding: utf-8 -*-
from datetime import datetime

db = DAL('postgres://beardcode:qazWSX11@localhost/fayol')

now = datetime.now()

db.define_table('language',
    Field('name', 'string', required=True, notnull=True),
    Field('code', 'string'),
    Field('locale', 'string'),
    Field('image', 'string'),
    Field('directory', 'string'),
    Field('filename', 'string'),
    Field('sort_order', 'integer', default=1),
    Field('status', 'boolean', default=True),
    Field('date_added', 'datetime'),
    Field('date_modified', 'datetime', default=now),
    migrate=False
)




