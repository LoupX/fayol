# -*- coding: utf-8 -*-

# Ajax functions.
def new_brand():
    pass

# Functions.
def create_brand(name):
    b = db.brands
    bd = db.brand_descriptions
    try:
        brand_id = db(b).insert()
        data = dict(brand_id=brand_id, name=name)
        brand_description_id = db.db.insert(**data)
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True

