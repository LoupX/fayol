# -*- coding: utf-8 -*-

@auth.requires_login()
def create_service():
    id = None
    data = dict()
    data_description = dict()
    vars = request.vars

    data['alternative_code'] = vars.alternative_code.decode('utf-8').upper()
    data['standard_cost'] = vars.standard_cost
    data['markup'] = vars.markup

    data_description['name'] = vars.name.decode('utf-8').upper()
    data_description['description'] = vars.description.decode('utf-8').upper()

    try:
        id = db.services.insert(**data)
        if id:
            data_description['service_id'] = id
            db.service_descriptions.insert(**data_description)
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
            code = 'SERV{}'.format(id)
            result = db(db.services.id==id).update(code=code)
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
def get_services():
    rows = None
    q = request.vars.query.upper() if request.vars.query else None
    try:
        query = db.services.status==True
        if q == 'ANY':
             query = db.services.id>0
        if q == 'FALSE':
            query = db.services.status==False
        query &= db.services.id==db.service_descriptions.service_id
        rows = db(query).select().as_list()
        for row in rows:
            id = row['services']['id']
            spl = db.service_price_lists
            row_price_list = db(spl.service_id==id).select(
                spl.id, spl.name, spl.price, spl.is_default,
                ppl.status).as_list()
            row['service_price_lists'] = row_price_list
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
def get_service_information():
    id = request.vars.id
    data = dict()
    row = None
    row_price_list = None
    try:
        query = db.services.id==id
        query &= db.services.id==db.service_descriptions.service_id
        row = db(query).select().as_list()
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
    if row_price_list:
        data['price_list'] = row_price_list
    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return str(data)

@auth.requires_login()
def update_service():
    id = request.vars.id
    data = dict()
    data_description = dict()
    vars = request.vars

    data['alternative_code'] = vars.alternative_code.decode('utf-8').upper()
    data['standard_cost'] = vars.standard_cost
    data['markup'] = vars.markup

    data_description['name'] = vars.name.decode('utf-8').upper()
    data_description['description'] = vars.description.decode('utf-8').upper()

    try:
        db(db.services.id==id).update(**data)
        db(db.service_descriptions.service_id==id).update(**data_description)
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
def toggle_service():
    id = request.vars.id
    try:
        row = db(db.products.id==id).select(db.products.status).first()
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

