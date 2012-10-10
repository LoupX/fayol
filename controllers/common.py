# -*- coding: utf-8 -*-

def get_states():
    s = db.states
    rows = db(s).select(s.id, s.name)
    options = []
    for row in rows:
        options += OPTION(row.name, _value=row.id)
    return options

def get_municipalities(state_id):
    m = db.municipalities
    query = m.state_id==state_id
    rows = db(query).select(m.id, m.name)
    options = []
    for row in rows:
        options += OPTION(row.name, _value=row.id)
    return options

def get_localities(state_id=None, municipality_id=None):
    l = db.localities
    m = db.municipalities
    options = []
    if state_id:
        query = m.state_id==state_id
        rows = db(query).select(m.id)
        mids = []
        for row in rows:
            mids.append(row.id)
        query = l.municipality_id.belongs(mids)
        rows = db(query).select(l.id, l.name)
        for row in rows:
            options += OPTION(row.name, _value=row.id)
    elif municipality_id:
        query = l.municipality_id==municipality_id
        rows = db(query).select(l.id, l.name)
        for row in rows:
            options += OPTION(row.name, _value=row.name)
    return options
