# -*- coding: utf-8 -*-

db.define_table('countries',
    Field('name'), migrate=MIGRATE)

db.define_table('states',
    Field('country_id', 'reference countries'),
    Field('name'),
    Field('hasc', length=5),
    Field('iso', length=3),
    Field('fips', length=4),
    Field('abbreviation', length=5),
    Field('inegi', length=2), migrate=MIGRATE)

db.define_table('municipalities',
    Field('state_id', 'reference states'),
    Field('name'),
    Field('inegi', length=3), migrate=MIGRATE)

db.define_table('localities',
    Field('municipality_id', 'reference municipalities'),
    Field('name'),
    Field('inegi', length=4), migrate=MIGRATE)

if db(db.countries).isempty():
    try:
        sqlite.define_table('countries',
            Field('name', 'string'),
            migrate=False)
        rows = sqlite().select(sqlite.countries.ALL).as_list()
        insert = []
        for row in rows:
            del row['id']
            insert.append(row)
        db.countries.bulk_insert(insert)
    except Exception as e:
        db.rollback()
        raise HTTP(500)
    else:
        db.commit()

if db(db.states).isempty():
    try:
        sqlite.define_table('states',
            Field('country_id'),
            Field('name'),
            Field('hasc', length=5),
            Field('iso', length=3),
            Field('fips', length=4),
            Field('abbreviation', length=5),
            Field('inegi', length=2),
            migrate=False)
        rows = sqlite().select(sqlite.states.ALL).as_list()
        insert = []
        for row in rows:
            del row['id']
            insert.append(row)
        db.states.bulk_insert(insert)
    except Exception as e:
        db.rollback()
        raise HTTP(500)
    else:
        db.commit()

if db(db.municipalities).isempty():
    try:
        sqlite.define_table('municipalities',
            Field('state_id'),
            Field('name'),
            Field('inegi', length=3),
            migrate=False)
        rows = sqlite().select(sqlite.municipalities.ALL).as_list()
        insert = []
        for row in rows:
            del row['id']
            insert.append(row)
        db.municipalities.bulk_insert(insert)
    except Exception as e:
        db.rollback()
        raise HTTP(500)
    else:
        db.commit()

if db(db.localities).isempty():
    try:
        sqlite.define_table('localities',
            Field('municipality_id'),
            Field('name'),
            Field('inegi', length=4),
            migrate=False)
        count = 0
        last = int(sqlite(sqlite.localities).count())
        while count < (last+1):
            insert = []
            rows = sqlite().select(sqlite.localities.ALL,
                limitby=(count,count+100)).as_list()
            for row in rows:
                del row['id']
                insert.append(row)
            db.localities.bulk_insert(rows)
            count += 100
    except Exception as e:
        db.rollback()
        raise HTTP(500)
    else:
        db.commit()
