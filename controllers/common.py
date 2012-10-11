# -*- coding: utf-8 -*-

def get_states():
    s = db.states
    rows = db(s).select(s.id, s.name)
    options = str()
    for row in rows:
        options += str(OPTION(row.name, _value=row.id))
        options += '\n'
    return options

def get_municipalities():
    m = db.municipalities
    options = str()
    if request.vars.id:
        id = request.vars.id
        query = m.state_id==id
        rows = db(query).select(m.id, m.name)
        for row in rows:
            options += str(OPTION(row.name, _value=row.id))
            options += '/n'
    return options

def get_localities():
    l = db.localities
    m = db.municipalities
    options = str()
    if request.vars.state_id:
        state_id = request.vars.state_id
        query = m.state_id==state_id
        rows = db(query).select(m.id)
        mids = []
        for row in rows:
            mids.append(row.id)
        query = l.municipality_id.belongs(mids)
        rows = db(query).select(l.id, l.name)
        for row in rows:
            options += str(OPTION(row.name, _value=row.id))
            options += '\n'
    elif request.vars.municipality_id:
        municipality_id = request.vars.municipality_id
        query = l.municipality_id==municipality_id
        rows = db(query).select(l.id, l.name)
        for row in rows:
            options += str(OPTION(row.name, _value=row.name))
            options += '\n'
    return options
