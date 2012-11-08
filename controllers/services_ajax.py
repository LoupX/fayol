# -*- coding: utf-8 -*-

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
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


@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def create_price():
    data = dict()
    v = request.vars
    if v.service_id:
        data['service_id'] = v.service_id
    else:
        return ''
    if v.name:
        data['name'] = v.name.decode('utf-8').upper()
    else:
        return ''
    if v.price:
        try:
            if float(v.price) > 0:
                data['price'] = v.price
        except:
            return ''
    else:
        return ''

    try:
        c = db(db.service_price_lists.service_id==data['service_id']).count()
    except:
        db.rollback()
        return ''
    else:
        if c >= 10:
            return '0'

    try:
        query = db.service_price_lists.service_id==data['service_id']
        rows = db(query).select()
        if not rows:
            data['is_default'] = True
    except:
        db.rollback()

    try:
        id = db.service_price_lists.insert(**data)
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        return str(id)


@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
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
            pl = db.service_price_lists
            row_price_list = db(pl.service_id==id).select(
                pl.id, pl.name, pl.price, pl.is_default,
                pl.status).as_list()
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


@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
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


@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def get_price():
    id = request.vars.id
    data = dict()
    pl = db.service_price_lists
    try:
        data = db(pl.service_id==id).select(
            pl.id, pl.name, pl.price, pl.status,
            pl.is_default, pl.service_id).as_list()
    except:
        db.rollback()

    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return str(data)


@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
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


@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
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
            if float(v.price) > 0:
                data['price'] = v.price
        except:
            return ''
    else:
        return ''

    try:
        query = db.service_price_lists.id==id
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


@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def update_default_price():
    id = request.vars.id
    try:
        service_id = db(db.service_price_lists.id==id).select(
            db.service_price_lists.service_id).first()
        service_id = service_id.service_id
        db(db.service_price_lists.service_id==service_id).update(
            is_default=False)
        result = db(db.service_price_lists.id==id).update(is_default=True)
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


@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def toggle_service():
    id = request.vars.id
    try:
        row = db(db.services.id==id).select(db.services.status).first()
        result = db(db.services.id==id).update(status=(not row.status))
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        if result == 1:
            return True
        else:
            return ''


@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def toggle_price():
    id = request.vars.id
    pl = db.service_price_lists
    try:
        row = db(pl.id==id).select(pl.status).first()
        result = db(pl.id==id).update(status=(not row.status))
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        if result == 1:
            return True
        else:
            return ''

