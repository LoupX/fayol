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
def create_product():
    data = dict()
    data_description = dict()

    data['brand_id'] = None
    data['unit_id'] = None
    data['code'] = None
    data['alternative_code'] = None
    data['location'] = None
    data['part_number'] = None
    data['serial_number'] = None
    data['model'] = None
    data['standard_cost'] = None
    data['markup'] = None

    data_description['name'] = None
    data_description['alternative_name'] = None
    data_description['description'] = None



@auth.requires_login()
def get_brands():
    data = []
    try:
        data = db(db.brand_descriptions.brand_id==
                 db.brands.id).select().as_list()
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
    try:
        data = db(db.category_descriptions.category_id==
                 db.categories.id).select().as_list()
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
    try:
        data = db(db.units).select().as_list()
    except:
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
def update_brand():
    data = dict()
    id = request.vars.id
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
