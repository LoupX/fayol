# -*- coding: utf-8 -*-

@auth.requires_login()
def create_package():
    data = dict()
    data_description = dict()
    vars = request.vars

    data['standard_cost'] = vars.standard_cost
    data['markup'] = vars.markup

    data_description['name'] = vars.name
    data_description['description'] = vars.description

    try:
        id = db.packages.insert(**data)
        code = 'PACK{}'.format(id)
        db(db.packages.id==id).update(code=code)
        data_description['package_id'] = id
        db.package_descriptions.insert(**data_description)
    except SyntaxError as e:
        db.rollback()
        if 'duplicate field' in e:
            return 0
        else:
            return ''
    except:
        db.rollback()
        return ''
    else:
        db.commit()
        return str(id)

@auth.requires_login()
def create_package_product():
    id = request.vars.id
    products = request.vars.products

@auth.requires_login()
def create_price():
    data = dict()
    v = request.vars
    if v.package_id:
        data['package_id'] = v.package_id
    if v.name:
        data['name'] = v.name.decode('utf-8').upper()
    data['price'] = v.price

    try:
        c = db(db.package_price_lists.package_id==data['package_id']).count()
    except:
        db.rollback()
    else:
        if c >= 10:
            return '0'

    try:
        query = db.package_price_lists.package_id==data['package_id']
        rows = db(query).select()
        if not rows:
            data['is_default'] = True
    except:
        db.rollback()

    try:
        id = db.package_price_lists.insert(**data)
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        return str(id)
