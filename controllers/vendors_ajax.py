# -*- coding: utf-8 -*-

def get_vendors():
    v = db.vendors
    q = request.vars.query
    query = v
    if q == 'TRUE':
        query = v.status==True
    elif q == 'FALSE':
        query = v.status==False
    rows = db(query).select(v.name, v.id)
    options = str()
    for row in rows:
        options += str(OPTION(row.name, _value=row.id))
        options += '\n'
    return options


def get_vendor_information():
    id = request.vars.id
    data = dict()
    try:
        id = int(id)
    except:
        return ''

    query = db.vendors.id==id
    row = db(query).select().as_list()

    if row:
        data = row[0]
    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return data

def create_vendor():
    data = dict()
    insert = dict()
    vars = request.vars
    data['name'] = vars.company
    data['address'] = vars.address
    data['state_id'] = vars.state
    data['municipality_id'] = vars.municipality
    data['locality_id'] = vars.locality
    data['zip_code'] = vars.zip_code
    data['rfc'] = vars.rfc
    data['website'] = vars.website
    for k, v in data.items():
        if v:
            insert[k] = v
    try:
        id = db.vendors.insert(**insert)
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        return str(id)

def update_vendor():
    vars = request.vars
    data = dict()
    id = vars.id
    data['name'] = vars.company
    data['address'] = vars.address
    data['state_id'] = vars.state
    data['municipality_id'] = vars.municipality
    data['locality_id'] = vars.locality
    data['zip_code'] = vars.zip_code
    data['rfc'] = vars.rfc
    data['website'] = vars.website
    result = _update_vendor(id, data)
    return result

def update_pay_information():
    data = dict()
    vars = request.vars
    id = vars.id
    data['bank_id'] = vars.bank_id
    data['branch'] = vars.branch
    data['bank_account_number'] = vars.account_number
    data['clabe'] = vars.clabe
    result = _update_vendor(id, data)
    return result

def toggle_vendor_status():
    id = request.vars.id
    status = request.vars.status
    status = True if status == 'True' else False
    data = dict(status=(not status))
    result = _update_vendor(id, data)
    return result

def _update_vendor(id, data):
    v = db.vendors
    query = v.id==id
    try:
        result = db(query).update(**data)
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        if result == 1:
            return True
        else:
            return ''
