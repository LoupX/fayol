# -*- coding: utf-8 -*-

def get_states():
    s = db.states
    rows = []
    try:
        rows = db(s).select(s.id, s.name)
    except:
        db.rollback()
    options = str()
    for row in rows:
        options += str(OPTION(row.name, _value=row.id))
        options += '\n'
    return options

def get_municipalities():
    m = db.municipalities
    options = str()
    rows = []
    if request.vars.id:
        id = request.vars.id
        query = m.state_id==id
        try:
            rows = db(query).select(m.id, m.name)
        except:
            db.rollback()
        for row in rows:
            options += str(OPTION(row.name, _value=row.id))
            options += '/n'
    return options

def get_localities():
    l = db.localities
    m = db.municipalities
    options = str()
    rows = []
    if request.vars.state_id:
        state_id = request.vars.state_id
        query = m.state_id==state_id
        try:
            rows = db(query).select(m.id)
        except:
            db.rollback()
        mids = []
        for row in rows:
            mids.append(row.id)
        query = l.municipality_id.belongs(mids)
        try:
            rows = db(query).select(l.id, l.name)
        except:
            db.rollback()
        for row in rows:
            options += str(OPTION(row.name, _value=row.id))
            options += '\n'
    elif request.vars.municipality_id:
        municipality_id = request.vars.municipality_id
        query = l.municipality_id==municipality_id
        try:
            rows = db(query).select(l.id, l.name)
        except:
            db.rollback()
        for row in rows:
            options += str(OPTION(row.name, _value=row.id))
            options += '\n'
    return options

def get_banks():
    b = db.banks
    rows = []
    try:
        rows = db(b).select(b.id, b.short_name)
    except:
        db.rollback()
    options = str()
    for row in rows:
        options += str(OPTION(row.short_name, _value=row.id))
        options += '\n'
    return options

def echo():
    return str(request.vars)
