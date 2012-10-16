# -*- coding: utf-8 -*-
@auth.requires_login()

def create_category():
    data = dict()
    if request.vars.name:
        data['name'] = request.vars.name
    data['description'] = request.vars.description
    try:
        c_id = db.categories.insert()
        cd_id = db.category_descriptions.insert(category_id=c_id, **data)
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
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        return str(id)

def create_brand():
    data = dict()
    if request.vars.name:
        data['name'] = request.vars.name
    data['description'] = request.vars.description
    try:
        b_id = db.brands.insert()
        bd_id = db.brand_descriptions.insert(brand_id=b_id, **data)
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        return str(dict(brand_id=b_id, brand_description_id=bd_id))

