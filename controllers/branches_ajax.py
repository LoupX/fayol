# -*- coding: utf-8 -*-

def get_branches():
    b = db.branches
    q = request.vars.query
    query = b.status==True
    if q == 'ANY':
        query = b
    elif q == 'FALSE':
        query = b.status==False
    try:
        rows = db(query).select(b.name, b.id)
    except:
        db.rollback()
    options = str()
    for row in rows:
        options += str(OPTION(row.name, _value=row.id))
        options += '\n'
    return options

def get_warehouses():
    w = db.warehouses
    q = request.vars.query
    query = w.status==True
    if q == 'ANY':
        query = w
    elif q == 'FALSE':
        query = w.status==False
    try:
        rows = db(query).select(w.name, w.id)
    except:
        db.rollback()
    options = str()
    for row in rows:
        options += str(OPTION(row.name, _value=row.id))
        options += '\n'
    return options

def get_branch_information():
    id = request.vars.id
    data = dict()
    try:
        query = db.branches.id==id
        query &= db.branches.company_address_id==db.company_addresses.id
        left = []
        left.append(db.states.on(db.branches.state_id == db.states.id))
        left.append(db.municipalities.on(
            db.branches.municipality_id == db.municipalities.id))
        left.append(
            db.localities.on(db.branches.locality_id == db.localities.id))
        left.append(db.banks.on(db.branches.bank_id == db.banks.id))
        left.append(db.company_tax_info.on(
            db.branches.company_tax_info_id==db.company_tax_info.id))
        row = db(query).select(
            db.branches.ALL, db.states.name, db.municipalities.name,
            db.localities.name, db.banks.short_name,
            db.company_addresses.ALL, db.company_tax_info.ALL,
            left=left).as_list()
    except:
        db.rollback()

    if row:
        data = row[0]
        if 'date_added' in data['branches']:
            data['branches']['date_added'] = str(
                data['branches']['date_added'])
        if 'date_modified' in data['branches']:
            data['branches']['date_modified'] = str(
                data['branches']['date_modified'])

    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return str(data)

def get_warehouse_information():
    id = request.vars.id
    data = dict()
    try:
        query = db.warehouses.id==id
        query &= db.warehouses.company_address_id==db.company_addresses.id
        left = []
        left.append(db.states.on(db.warehouses.state_id == db.states.id))
        left.append(db.municipalities.on(
            db.warehouses.municipality_id == db.municipalities.id))
        left.append(
            db.localities.on(db.warehouses.locality_id == db.localities.id))
        left.append(db.banks.on(db.warehouses.bank_id == db.banks.id))
        left.append(db.company_tax_info.on(
            db.warehouses.company_tax_info_id==db.company_tax_info.id))
        row = db(query).select(
            db.warehouses.ALL, db.states.name, db.municipalities.name,
            db.localities.name, db.banks.short_name,
            db.company_addresses.ALL, left=left).as_list()
    except:
        db.rollback()

    if row:
        data = row[0]
        if 'date_added' in data['branches']:
            data['warehouses']['date_added'] = str(
                data['warehouses']['date_added'])
        if 'date_modified' in data['branches']:
            data['warehouses']['date_modified'] = str(
                data['warehouses']['date_modified'])

    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return str(data)

def create_branch():
    data = dict()
    data_address = dict()
    data_tax = dict()
    vars = request.vars
    tax_info_id = None

    data_address['address'] = vars.address
    data_address['suburb'] = vars.suburb
    data_address['state_id'] = vars.states
    data_address['municipality_id'] = vars.municipality
    data_address['locality_id'] = vars.locality
    data_address['zip_code'] = vars.zip_code

    if vars.corporate:
        data_tax['business_name'] = vars.corporate
    if vars.rfc:
        data_tax['rfc'] = vars.rfc
    if vars.tax_regime:
        data_tax['tax'] = vars.tax_regime

    data['name'] = vars.name

    try:
        address_id = db.company_addresses.insert(**data_address)
        if data_tax:
            tax_info_id = db.company_tax_info.insert(**data_tax)
    except Exception as e:
        db.rollback()
        return ''
    else:
        try:
            data['company_address_id'] = address_id
            if tax_info_id:
                data['company_tax_info_id'] = tax_info_id
            id = db.branches.insert(**data)
        except Exception as e:
            db.rollback()
            return ''
        else:
            db.commit()
            return str(id)


def create_warehouse():
    data = dict()
    data_address = dict()
    vars = request.vars
    tax_info_id = None

    data_address['address'] = vars.address
    data_address['suburb'] = vars.suburb
    data_address['state_id'] = vars.states
    data_address['municipality_id'] = vars.municipality
    data_address['locality_id'] = vars.locality
    data_address['zip_code'] = vars.zip_code

    data['name'] = vars.name

    try:
        address_id = db.company_addresses.insert(**data_address)
    except Exception as e:
        db.rollback()
        return ''
    else:
        try:
            data['company_address_id'] = address_id
            id = db.warehouses.insert(**data)
        except Exception as e:
            db.rollback()
            return ''
        else:
            db.commit()
            return str(id)
