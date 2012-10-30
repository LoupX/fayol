# -*- coding: utf-8 -*-

@auth.requires_login()
def create_package():
    id = None
    data = dict()
    data_description = dict()
    vars = request.vars

    data['alternative_code'] = vars.alternative_code.decode('utf-8').upper()
    data['standard_cost'] = vars.standard_cost
    data['markup'] = vars.markup

    data_description['name'] = vars.name.decode('utf-8').upper()
    data_description['alternative_name'] = vars.alternative_name.decode('utf-8').upper()
    data_description['description'] = vars.description.decode('utf-8').upper()

    try:
        id = db.packages.insert(**data)
        if id:
            data_description['product_id'] = id
            db.package_descriptions.insert(**data_description)
            if vars['products[]']:
                for k in vars['products8[]']:
                    db.product_to_vendor.insert(product_id=id,
                        vendor_id=k)
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
        try:
            row_category = db(db.category_descriptions.category_id==
                vars.category_id).select().first()
            row_brand = db(db.brand_descriptions.brand_id==
                vars.brand_id).select().first()
            code = '{}{}{}'.format(
                row_category.name[0:2].decode('utf-8').upper(),
                row_brand.name[0:2].decode('utf-8').upper(), id)
            result = db(db.products.id==id).update(code=code)
        except Exception as e:
            db.rollback()
            return ''
        else:
            if result==1:
                db.commit()
                return str(id)
            else:
                db.rollback()
                return ''

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
