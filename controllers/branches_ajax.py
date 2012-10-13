# -*- coding: utf-8 -*-

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
        return e
    else:
        try:
            data['company_address_id'] = address_id
            if tax_info_id:
                data['company_tax_info_id'] = tax_info_id
            id = db.branches.insert(**data)
        except Exception as e:
            db.rollback()
            return e
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
        return e
    else:
        try:
            data['company_address_id'] = address_id
            id = db.warehouses.insert(**data)
        except Exception as e:
            db.rollback()
            return e
        else:
            db.commit()
            return str(id)

