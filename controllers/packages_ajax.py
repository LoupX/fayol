# -*- coding: utf-8 -*-

@auth.requires_login()
def create_package():
    data = dict()
    data_description = dict()
    vars = request.vars

    data['alternative_code'] = vars.alternative_code
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

@auth.requires_login()
def get_package_information():
    id = request.vars.id
    data = dict()
    row = None
    row_products = None
    row_price_list = None
    try:
        query = db.packages.id==id
        query &= db.packages.id==db.package_descriptions.package_id
        row = db(query).select().as_list()
        ptp = db.package_to_product()
        query = ptp.package_id==id
        query &= ptp.product_id==db.product_descriptions.product_id
        row_products = db(query).select(
            ptp.ALL, db.product_descriptions.name,
            db.product_descriptions.description).as_list()
        spl = db.service_price_lists
        row_price_list = db(spl.service_id==id).select(
            spl.id, spl.name, spl.price, spl.is_default,
            spl.status).as_list()
    except Exception as e:
        db.rollback()

    if row:
        data = row[0]
        import datetime
        for r in data:
            for k in data[r]:
                if type(data[r][k]) is datetime.datetime:
                    data[r][k] = str(data[r][k])
    if row_products:
        data['products'] = row_products
    if row_price_list:
        data['price_list'] = row_price_list
    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return str(data)

@auth.requires_login()
def update_package():
    vars = request.vars
    data = dict()
    data_description = dict()

    package_id = vars.package_id
    data['alternative_code'] = vars.alternative_code
    data['standard_cost'] = vars.standard_cost
    data['markup'] = vars.markup

    package_description_id = vars.package_description_id
    data_description['name'] = vars.name
    data_description['description'] = vars.description

    try:
        result1 = db(db.packages.id==package_id).update(**data)
        result2 = db(db.package_descriptions.id==
           package_description_id).update(**data_description)
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
        if result1 == 1 and result2 == 1:
            db.commit()
            return True
        else:
            db.rollback()
            return ''


@auth.requires_login()
def update_package_product():
    pass

@auth.requires_login()
def update_price():
    id = request.vars.id
    data = dict()
    if request.vars.name:
        data['name'] = request.vars.name.decode('utf-8').upper()
    data['price'] = request.vars.price
    try:
        query = db.package_price_lists.id==id
        result = db(query).update(**data)
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        if result == 1:
            return True
        else:
            db.rollback()
            return ''

@auth.requires_login()
def update_default_price():
    id = request.vars.id
    try:
        package_id = db(db.package_price_lists.id==id).select(
            db.package_price_lists.package_id).first()
        package_id = package_id.service_id
        db(db.package_price_lists.package_id==package_id).update(
            is_default=False)
        result = db(db.package_price_lists.id==id).update(is_default=True)
    except Exception as e:
        db.rollback()
        return ''
    else:
        if result == 1:
            db.commit()
            return True
        else:
            db.rollback()
            return ''

@auth.requires_login()
def toggle_package():
    id = request.vars.id
    try:
        row = db(db.packages.id==id).select().first()
        result = db(db.packages.id==id).update(status=(not row.status))
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        if result == 1:
            return True
        else:
            return ''