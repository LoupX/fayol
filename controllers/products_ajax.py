# -*- coding: utf-8 -*-

@auth.requires_login()
def create_brand():
    data = dict()
    if request.vars.name:
        data['name'] = request.vars.name.decode('utf-8').upper()
    data['description'] = request.vars.description.decode('utf-8').upper()
    try:
        b_id = db.brands.insert()
        bd_id = db.brand_descriptions.insert(brand_id=b_id, **data)
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
        return str(dict(brand_id=b_id, brand_description_id=bd_id))

@auth.requires_login()
def create_category():
    data = dict()
    if request.vars.name:
        data['name'] = request.vars.name.decode('utf-8').upper()
    data['description'] = request.vars.description.decode('utf-8').upper()
    try:
        c_id = db.categories.insert()
        cd_id = db.category_descriptions.insert(category_id=c_id, **data)
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
        return str(dict(category_id=c_id, category_description_id=cd_id))

@auth.requires_login()
def create_unit():
    data = dict()
    if request.vars.measuring_unit and request.vars.abbreviation:
        data['name'] = request.vars.measuring_unit.decode('utf-8').upper()
        data['abbreviation'] = request.vars.abbreviation.decode('utf-8').upper()
    try:
        id = db.units.insert(**data)
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
def create_price():
    data = dict()
    v = request.vars
    if v.product_id:
        data['product_id'] = v.product_id

    if v.name:
        data['name'] = v.name.decode('utf-8').upper()
    else:
        return ''
    if v.price:
        try:
            if int(v.price) > 0:
                data['price'] = v.price
        except:
            return ''
    else:
        return ''

    try:
        c = db(db.product_price_lists.product_id==data['product_id']).count()
    except:
        db.rollback()
        return ''
    else:
        if c >= 10:
            return '0'

    try:
        query = db.product_price_lists.product_id==data['product_id']
        rows = db(query).select()
        if not rows:
            data['is_default'] = True
    except:
        db.rollback()

    try:
        id = db.product_price_lists.insert(**data)
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        return str(id)

@auth.requires_login()
def create_product():
    id = None
    data = dict()
    data_description = dict()
    vars = request.vars

    data['brand_id'] = vars.brand_id
    data['unit_id'] = vars.unit_id
    data['category_id'] = vars.category_id
    data['alternative_code'] = vars.alternative_code.decode('utf-8').upper()
    data['part_number'] = vars.part_number.decode('utf-8').upper()
    data['serial_number'] = vars.serial_number.decode('utf-8').upper()
    data['model'] = vars.model.decode('utf-8').upper()
    data['standard_cost'] = vars.standard_cost
    data['markup'] = vars.markup

    data_description['name'] = vars.name.decode('utf-8').upper()
    data_description['alternative_name'] = vars.alternative_name.decode('utf-8').upper()
    data_description['description'] = vars.description.decode('utf-8').upper()

    try:
        id = db.products.insert(**data)
        if id:
            data_description['product_id'] = id
            db.product_descriptions.insert(**data_description)
            if vars['vendors[]']:
                for k in vars['vendors[]']:
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
def get_brands():
    data = []
    q = request.vars.query.upper() if request.vars.query else None
    try:
        query = db.brand_descriptions.brand_id==db.brands.id
        if q == 'ANY':
            query = db.brand_descriptions.brand_id==db.brands.id
        elif q == 'FALSE':
            query &= db.brands.status==False
        else:
            query &= db.brands.status==True
        data = db(query).select().as_list()
    except:
        db.rollback()

    if data:
        import datetime
        for row in data:
            for k in row:
                for key in row[k]:
                    if type(row[k][key]) is datetime.datetime:
                        row[k][key] = str(row[k][key])
    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return str(data)

@auth.requires_login()
def get_categories():
    data = []
    q = request.vars.query.upper() if request.vars.query else None
    try:
        query = db.category_descriptions.category_id==db.categories.id
        if q == 'ANY':
            query = db.category_descriptions.category_id==db.categories.id
        elif q == 'FALSE':
            query &= db.categories.status==False
        else:
            query &= db.categories.status==True
        data = db(query).select().as_list()
    except:
        db.rollback()

    if data:
        import datetime
        for row in data:
            for k in row:
                for key in row[k]:
                    if type(row[k][key]) is datetime.datetime:
                        row[k][key] = str(row[k][key])
    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return str(data)

@auth.requires_login()
def get_units():
    data = []
    q = request.vars.query.upper() if request.vars.query else None
    try:
        query = db.units.status==True
        if q == 'ANY':
            query = db.units
        elif q == 'FALSE':
            query = db.units.status==False
        data = db(query).select().as_list()
    except Exception as e:
        db.rollback()

    if data:
        import datetime
        for row in data:
            for k in row:
                if type(row[k]) is datetime.datetime:
                    row[k] = str(row[k])
    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return str(data)

@auth.requires_login()
def get_products():
    rows = None
    q = request.vars.query.upper() if request.vars.query else None
    try:
        query = db.products.status==True
        if q == 'ANY':
             query = db.products.id>0
        if q == 'FALSE':
            query = db.products.status==False
        query &= db.products.id==db.product_descriptions.product_id
        query &= db.products.brand_id==db.brand_descriptions.brand_id
        query &= db.products.category_id==db.category_descriptions.category_id
        query &= db.products.unit_id==db.units.id
        rows = db(query).select().as_list()
        for row in rows:
            id = row['products']['id']
            query_vendors = db.product_to_vendor.product_id==id
            query_vendors &= db.vendors.id==db.product_to_vendor.vendor_id
            query_vendors &= db.products.id==db.product_to_vendor.product_id
            row_vendors = db(query_vendors).select(db.vendors.id,
                db.vendors.name).as_list()
            ppl = db.product_price_lists
            row_price_list = db(ppl.product_id==id).select(
                ppl.id, ppl.name, ppl.price, ppl.is_default,
                ppl.status).as_list()
            row['vendors'] = row_vendors
            row['product_price_lists'] = row_price_list
    except Exception as e:
        db.rollback()
    if rows:
        import datetime
        for row in rows:
            for key in row:
                for k in row[key]:
                    if (type(k) is str and
                        type(row[key][k]) is datetime.datetime):
                        row[key][k] = str(row[key][k])
    from gluon.contrib import simplejson
    rows = simplejson.dumps(rows)
    return str(rows)

@auth.requires_login()
def get_product_information():
    id = request.vars.id
    data = dict()
    row = None
    row_vendors = None
    row_price_list = None
    try:
        query = db.products.id==id
        query &= db.products.id==db.product_descriptions.product_id
        query &= db.products.brand_id==db.brand_descriptions.brand_id
        query &= db.products.category_id==db.category_descriptions.category_id
        query &= db.products.unit_id==db.units.id
        row = db(query).select().as_list()
        query_vendors = db.product_to_vendor.product_id==id
        query_vendors &= db.vendors.id==db.product_to_vendor.vendor_id
        query_vendors &= db.products.id==db.product_to_vendor.product_id
        row_vendors = db(query_vendors).select(db.vendors.id,
            db.vendors.name).as_list()
        ppl = db.product_price_lists
        row_price_list = db(ppl.product_id==id).select(
            ppl.id, ppl.name, ppl.price, ppl.is_default,
            ppl.status).as_list()
    except Exception as e:
        db.rollback()

    if row:
        data = row[0]
        import datetime
        for r in data:
            for k in data[r]:
                if type(data[r][k]) is datetime.datetime:
                    data[r][k] = str(data[r][k])
    if row_vendors:
        data['vendors'] = row_vendors
    if row_price_list:
        data['price_list'] = row_price_list
    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return str(data)


@auth.requires_login()
def update_brand():
    data = dict()
    id = request.vars.id
    if request.vars.name:
        data['name'] = request.vars.name.decode('utf-8').upper()
    data['description'] = request.vars.description.decode('utf-8').upper()
    try:
        result = db(db.brand_descriptions.brand_id==id).update(**data)
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

@auth.requires_login()
def update_category():
    data = dict()
    id = request.vars.id
    if request.vars.name:
        data['name'] = request.vars.name.decode('utf-8').upper()
    data['description'] = request.vars.description.decode('utf-8').upper()
    try:
        result = db(db.category_descriptions.category_id==id).update(**data)
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


@auth.requires_login()
def update_unit():
    data = dict()
    id = request.vars.id
    if request.vars.name:
        data['name'] = request.vars.name.decode('utf-8').upper()
    data['abbreviation'] = request.vars.abbreviation.decode('utf-8').upper()
    try:
        result = db(db.units.id==id).update(**data)
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

@auth.requires_login()
def update_default_price():
    id = request.vars.id
    try:
        product_id = db(db.product_price_lists.id==id).select(
            db.product_price_lists.product_id).first()
        product_id = product_id.product_id
        db(db.product_price_lists.product_id==product_id).update(
            is_default=False)
        result = db(db.product_price_lists.id==id).update(is_default=True)
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
def update_price():
    id = request.vars.id
    data = dict()
    v = request.vars

    if v.name:
        data['name'] = v.name.decode('utf-8').upper()
    else:
        return ''
    if v.price:
        try:
            if int(v.price) > 0:
                data['price'] = v.price
        except:
            return ''
    else:
        return ''

    try:
        query = db.product_price_lists.id==id
        result = db(query).update(**data)
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
def update_product():
    id = request.vars.id
    data = dict()
    data_description = dict()
    vars = request.vars

    data['brand_id'] = vars.brand_id
    data['unit_id'] = vars.unit_id
    data['category_id'] = vars.category_id
    data['alternative_code'] = vars.alternative_code.decode('utf-8').upper()
    data['part_number'] = vars.part_number.decode('utf-8').upper()
    data['serial_number'] = vars.serial_number.decode('utf-8').upper()
    data['model'] = vars.model.decode('utf-8').upper()
    data['standard_cost'] = vars.standard_cost
    data['markup'] = vars.markup

    row_category = db(db.category_descriptions.category_id==
                      vars.category_id).select().first()
    row_brand = db(db.brand_descriptions.brand_id==
                   vars.brand_id).select().first()
    code = '{}{}{}'.format(
        row_category.name[0:2].decode('utf-8').upper(),
        row_brand.name[0:2].decode('utf-8').upper(), id)

    data['code'] = code

    data_description['name'] = vars.name.decode('utf-8').upper()
    data_description['alternative_name'] = vars.alternative_name.decode('utf-8').upper()
    data_description['description'] = vars.description.decode('utf-8').upper()

    try:
        db(db.products.id==id).update(**data)
        db(db.product_descriptions.product_id==id).update(**data_description)
        db(db.product_to_vendor.product_id==id).delete()
        if vars['vendors[]']:
            for k in vars['vendors[]']:
                db.product_to_vendor.insert(product_id=id,
                    vendor_id=k)
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
        return True

@auth.requires_login()
def toggle_brand():
    id = request.vars.id
    try:
        row = db.brands[id]
        result = db(db.brands.id==id).update(status=(not row.status))
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
def toggle_category():
    id = request.vars.id
    try:
        row = db(db.categories.id==id).select().first()
        result = db(db.categories.id==id).update(status=(not row.status))
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
def toggle_unit():
    id = request.vars.id
    try:
        row = db(db.units.id==id).select().first()
        result = db(db.units.id==id).update(status=(not row.status))
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
def toggle_product():
    id = request.vars.id
    try:
        row = db(db.products.id==id).select().first()
        result = db(db.products.id==id).update(status=(not row.status))
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        if result == 1:
            return True
        else:
            return ''
