# -*- coding: utf-8 -*-

@auth.requires_login()
def get_branches():
    b = db.branches
    q = request.vars.query
    query = b.status==True
    rows = []
    if q == 'ANY':
        query = b
    elif q == 'FALSE':
        query = b.status == False
    try:
        rows = db(query).select(b.name, b.id)
    except:
        db.rollback()
    options = str()
    for row in rows:
        options += str(OPTION(row.name, _value=row.id))
        options += '\n'
    return options

@auth.requires_login()
def get_warehouses():
    w = db.warehouses
    q = request.vars.query
    query = w.status == True
    rows = []
    if q == 'ANY':
        query = w
    elif q == 'FALSE':
        query = w.status == False
    try:
        rows = db(query).select(w.name, w.id)
    except:
        db.rollback()
    options = str()
    for row in rows:
        options += str(OPTION(row.name, _value=row.id))
        options += '\n'
    return options

@auth.requires_login()
def get_branch_information():
    id = request.vars.id
    data = dict()
    row = None

    try:
        query = db.branches.id == id
        left = []
        left.append(db.company_addresses.on(
            db.branches.company_address_id == db.company_addresses.id))
        left.append(db.company_tax_info.on(
            db.branches.company_tax_info_id == db.company_tax_info.id))
        left.append(db.states.on(db.company_addresses.state_id == db.states.id))
        left.append(db.municipalities.on(
            db.company_addresses.municipality_id == db.municipalities.id))
        left.append(
            db.localities.on(
                db.company_addresses.locality_id == db.localities.id))
        row = db(query).select(
            db.branches.ALL, db.states.name, db.municipalities.name,
            db.localities.name, db.company_addresses.ALL,
            db.company_tax_info.ALL, left=left).as_list()
    except:
        db.rollback()

    import datetime
    if row:
        data = row[0]
        for r in data:
            for k in data[r]:
                if type(data[r][k]) is datetime.datetime:
                    data[r][k] = str(data[r][k])

    from gluon.contrib import simplejson

    data = simplejson.dumps(data)
    return str(data)

@auth.requires_login()
def get_warehouse_information():
    id = request.vars.id
    data = dict()
    row = None
    try:
        query = db.warehouses.id == id
        left = []
        left.append(db.company_addresses.on(
            db.warehouses.company_address_id == db.company_addresses.id))
        left.append(db.states.on(db.company_addresses.state_id == db.states.id))
        left.append(db.municipalities.on(
            db.company_addresses.municipality_id == db.municipalities.id))
        left.append(
            db.localities.on(
                db.company_addresses.locality_id == db.localities.id))
        row = db(query).select(
            db.warehouses.ALL, db.states.name,
            db.municipalities.name, db.localities.name,
            db.company_addresses.ALL, left=left).as_list()
    except:
        db.rollback()

    import datetime

    if row:
        data = row[0]
        for r in data:
            for k in data[r]:
                if type(data[r][k]) is datetime.datetime:
                    data[r][k] = str(data[r][k])

    from gluon.contrib import simplejson

    data = simplejson.dumps(data)
    return str(data)

@auth.requires_login()
def create_branch():
    data = dict()
    data_address = dict()
    data_tax = dict()
    vars = request.vars

    data_address['address'] = vars.address.decode('utf-8').upper()
    data_address['suburb'] = vars.suburb.decode('utf-8').upper()
    data_address['state_id'] = vars.states
    data_address['municipality_id'] = vars.municipality
    data_address['locality_id'] = vars.locality
    data_address['zip_code'] = vars.zip_code

    data_tax['business_name'] = vars.corporate.decode('utf-8').upper()
    data_tax['rfc'] = vars.rfc.decode('utf-8').upper()
    data_tax['tax'] = vars.tax_regime.decode('utf-8').upper()

    data['name'] = vars.name.decode('utf-8').upper()

    try:
        address_id = db.company_addresses.insert(**data_address)
        tax_info_id = db.company_tax_info.insert(**data_tax)
    except Exception as e:
        db.rollback()
        return ''
    else:
        try:
            data['company_address_id'] = address_id
            data['company_tax_info_id'] = tax_info_id
            id = db.branches.insert(**data)
        except SyntaxError as e:
            db.rollback()
            if 'duplicate field' in e:
                return 0
            else:
                return e
        except Exception as e:
            db.rollback()
            return ''
        else:
            db.commit()
            return str(id)

@auth.requires_login()
def create_warehouse():
    data = dict()
    data_address = dict()
    vars = request.vars

    data_address['address'] = vars.address.decode('utf-8').upper()
    data_address['suburb'] = vars.suburb.decode('utf-8').upper()
    data_address['state_id'] = vars.states
    data_address['municipality_id'] = vars.municipality
    data_address['locality_id'] = vars.locality
    data_address['zip_code'] = vars.zip_code
    data['name'] = vars.name.decode('utf-8').upper()

    try:
        address_id = db.company_addresses.insert(**data_address)
    except Exception as e:
        db.rollback()
        return ''
    else:
        try:
            data['company_address_id'] = address_id
            id = db.warehouses.insert(**data)
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

@auth.requires_login()
def toggle_branch_status():
    id = request.vars.id
    status = str(request.vars.status).upper()
    status = True if status == 'TRUE' else False
    data = dict(status=(not status))
    try:
        result = db(db.branches.id==id).update(**data)
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        if result == 1:
            return True
        else:
            return ''

@auth.requires_login()
def toggle_warehouse_status():
    id = request.vars.id
    status = str(request.vars.status).upper()
    status = True if status == 'TRUE' else False
    data = dict(status=(not status))
    try:
        result = db(db.warehouses.id==id).update(**data)
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        if result == 1:
            return True
        else:
            return ''

@auth.requires_login()
def update_branch():
    b = db.branches
    vars = request.vars
    id = vars.id
    data = dict()
    data_address = dict()
    data_tax = dict()
    try:
        row = db(db.branches.id==id).select(db.branches.company_address_id,
            db.branches.company_tax_info_id).first()
        company_address_id = row.company_address_id
        company_tax_info_id = row.company_tax_info_id
    except Exception as e:
        db.rollback()
        return ''

    data_address['address'] = vars.address.decode('utf-8').upper()
    data_address['suburb'] = vars.suburb.decode('utf-8').upper()
    data_address['state_id'] = vars.state
    data_address['municipality_id'] = vars.municipality
    data_address['locality_id'] = vars.locality
    data_address['zip_code'] = vars.zip_code

    data_tax['business_name'] = vars.business_name.decode('utf-8').upper()
    data_tax['rfc'] = vars.rfc.decode('utf-8').upper()
    data_tax['tax'] = vars.tax.decode('utf-8').upper()

    data['name'] = vars.name

    try:
        db(db.branches.id==id).update(**data)
        db(db.company_addresses.id==company_address_id).update(**data_address)
        db(db.company_tax_info.id==company_tax_info_id).update(**data_tax)
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
        return True

@auth.requires_login()
def update_warehouse():
    b = db.branches
    vars = request.vars
    id = vars.id
    data = dict()
    data_address = dict()

    try:
        row = db(db.warehouses.id==id).select(
            db.warehouses.company_address_id).first()
        company_address_id = row.company_address_id
    except Exception as e:
        db.rollback()
        return ''

    data_address['address'] = vars.address.decode('utf-8').upper()
    data_address['suburb'] = vars.suburb.decode('utf-8').upper()
    data_address['state_id'] = vars.state
    data_address['municipality_id'] = vars.municipality
    data_address['locality_id'] = vars.locality
    data_address['zip_code'] = vars.zip_code

    data['name'] = vars.name.decode('utf-8').upper()

    try:
        db(db.warehouses.id==id).update(**data)
        db(db.company_addresses.id==company_address_id).update(**data_address)
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
        return True
