# -*- coding: utf-8 -*-

db.define_table('banks',
    Field('abm_number', 'string', length=3, notnull=True),
    Field('institution_name', 'string', notnull=True),
    Field('short_name', 'string', notnull=True),
    format='%(short_name)s')

if db(db.banks).isempty():
    try:
        sqlite.define_table('banks',
            Field('abm_number', 'string', length=3, notnull=True),
            Field('institution_name', 'string', notnull=True),
            Field('short_name', 'string', notnull=True),
            format='%(short_name)s',
            migrate=False)
        rows = sqlite().select(sqlite.banks.ALL).as_list()
        insert = []
        for row in rows:
            del row['id']
            insert.append(row)
        db.banks.bulk_insert(insert)
    except Exception as e:
        db.rollback()
        raise HTTP(503)
    else:
        db.commit()
