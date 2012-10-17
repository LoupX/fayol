# -*- coding: utf-8 -*-
@auth.requires_login()

def create_brand():
    data = dict()
    if request.vars.name:
        data['name'] = request.vars.name.upper()
    data['description'] = request.vars.description.upper()
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

def create_category():
    data = dict()
    if request.vars.name:
        data['name'] = request.vars.name
    data['description'] = request.vars.description
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

def create_unit():
    data = dict()
    if request.vars.measuring_unit and request.vars.abbreviation:
        data['name'] = request.vars.measuring_unit
        data['abbreviation'] = request.vars.abbreviation
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

def get_brands():
    data = []
    try:
        data = db(db.brand_descriptions.brand_id==
                 db.brands.id).select().as_list()
    except:
        db.rollback()

    import datetime
    if data:
        for row in data:
            for k in row:
                for key in row[k]:
                    if type(row[k][key]) is datetime.datetime:
                        row[k][key] = str(row[k][key])
    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return str(data)

