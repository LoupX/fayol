# -*- coding: utf-8 -*-

@auth.requires_membership('GOD', 'Administrador')
def get_vendors():
    v = db.vendors
    q = request.vars.query
    query = v.status==True
    rows = []
    if q == 'ANY':
        query = v
    elif q == 'FALSE':
        query = v.status==False
    try:
        rows = db(query).select(v.name, v.id)
    except:
        db.rollback()
    options = str()
    for row in rows:
        options += str(OPTION(row.name, _value=row.id))
        options += '\n'
    return options

@auth.requires_membership('GOD', 'Administrador')
def get_vendor_information():
    id = request.vars.id
    data = dict()
    row = None

    try:
        query = db.vendors.id==id
        left = []
        left.append(db.states.on(db.vendors.state_id==db.states.id))
        left.append(db.municipalities.on(
            db.vendors.municipality_id==db.municipalities.id))
        left.append(db.localities.on(db.vendors.locality_id==db.localities.id))
        left.append(db.banks.on(db.vendors.bank_id==db.banks.id))
        row = db(query).select(
            db.vendors.ALL, db.states.name, db.municipalities.name,
            db.localities.name, db.banks.short_name, left=left).as_list()
    except:
        db.rollback()

    if row:
        data = row[0]
        if 'date_added' in data['vendors']:
            data['vendors']['date_added'] = str(data['vendors']['date_added'])
        if 'date_modified' in data['vendors']:
            data['vendors']['date_modified'] = str(data['vendors']['date_modified'])

    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return str(data)

@auth.requires_membership('GOD', 'Administrador')
def create_vendor():
    data = dict()
    insert = dict()
    vars = request.vars
    data['name'] = vars.company.decode('utf-8').upper()
    data['address'] = vars.address.decode('utf-8').upper()
    data['state_id'] = vars.state
    data['municipality_id'] = vars.municipality
    data['locality_id'] = vars.locality
    data['zip_code'] = vars.zip_code
    data['rfc'] = vars.rfc.decode('utf-8').upper()
    data['website'] = vars.website.decode('utf-8').upper()
    for k, v in data.items():
        if v:
            insert[k] = v
    try:
        id = db.vendors.insert(**insert)
    except SyntaxError as e:
        db.rollback()
        if 'duplicate field' in e:
            return 0
        else:
            return ''
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        return str(id)

@auth.requires_membership('GOD', 'Administrador')
def update_vendor():
    vars = request.vars
    data = dict()
    id = vars.id
    data['name'] = vars.company.decode('utf-8').upper()
    data['address'] = vars.address.decode('utf-8').upper()
    data['state_id'] = vars.state
    data['municipality_id'] = vars.municipality
    data['locality_id'] = vars.locality
    data['zip_code'] = vars.zip_code
    data['rfc'] = vars.rfc.decode('utf-8').upper()
    data['website'] = vars.website.decode('utf-8').upper()
    result = _update_vendor(id, **data)
    return result

@auth.requires_membership('GOD', 'Administrador')
def update_pay_information():
    data = dict()
    vars = request.vars
    id = vars.id
    data['bank_id'] = vars.bank_id
    data['branch'] = vars.branch
    data['bank_account_number'] = vars.account_number
    data['clabe'] = vars.clabe
    result = _update_vendor(id, **data)
    return result

@auth.requires_membership('GOD', 'Administrador')
def toggle_vendor_status():
    id = request.vars.id
    status = str(request.vars.status).upper()
    status = True if status == 'TRUE' else False
    data = dict(status=(not status))
    result = _update_vendor(id, **data)
    return result

@auth.requires_membership('GOD', 'Administrador')
def _update_vendor(id, **data):
    v = db.vendors
    query = v.id==id
    try:
        result = db(query).update(**data)
    except SyntaxError as e:
        db.rollback()
        if 'duplicate field' in e:
            return 0
        else:
            return ''
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        if result == 1:
            return True
        else:
            return ''
