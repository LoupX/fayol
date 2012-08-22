# -*- coding: utf-8 -*-
from os.path import join

db.define_table('language',
    Field('name', 'string', required=True, notnull=True, label=T('Name')),
    Field('code', 'string', length=10, required=True, notnull=True, label=T('Code')),
    Field('locale', required=True, notnull=True, label=T('Locale')),
    Field('image', 'upload', required=True, notnull=True, uploadfield=True,label=T('Image')),
    Field('sort_order', 'integer', label=T('Sort order')),
    Field('status', 'boolean', default=True),
    Field('is_default', 'boolean', required=True, notnull=True, default=False, label=T('Default')),
    Field('date_added', 'datetime', writable=False, readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False, readable=False)
)

db.language.image.uploadfolder = join(request.folder, 'uploads/{}'.format(LANG_IMG_PATH))
db.language.date_added.represent = lambda date_added, row: date_added.strftime('%d - %m - %Y')
db.language.date_modified.represent = lambda date_modified, row: date_added.strftime('%d - %m - %Y')
