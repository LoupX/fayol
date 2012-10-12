# -*- coding: utf-8 -*-

def create_category():
    data = dict()
    if request.vars.category_name:
        data['name'] = request.vars.category_name
    data['description'] = request.vars.category_description
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
    pass

