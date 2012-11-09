# -*- coding: utf-8 -*-

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def create_client():
    id = None
    data = dict()

    data['first_name'] = request.vars.first_name
    data['last_name'] = request.vars.last_name
    data['rfc'] = request.vars.rfc
    data['phone'] = request.vars.phone
    data['mobile'] = request.vars.mobile
    if request.vars.state_id:
        data['state_id'] = request.vars.state_id
    if request.vars.municipality_id:
        data['municipality_id'] = request.vars.municipality_id
    if request.vars.locality_id:
        data['locality_id'] = request.vars.locality_id
    data['address'] = request.vars.address
    data['suburb'] = request.vars.suburb
    data['zip_code'] = request.vars.zip_code

    try:
        id = db.clients.insert(**data)
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


@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def get_clients():
    id = request.vars.id
    data = []

    try:
        data = db(db.clients).select().as_list()
    except:
        db.rollback()

    if data:
        for k in data:
            k['date_added'] = str(k['date_added'])
            k['date_modified'] = str(k['date_modified'])
    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return str(data)
