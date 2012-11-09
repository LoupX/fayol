# -*- coding: utf-8 -*-

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def create_client():
    id = None
    data = dict()

    data['first_name'] = request.vars.first_name.decode('utf-8').upper()
    data['last_name'] = request.vars.last_name.decode('utf-8').upper()
    data['rfc'] = request.vars.rfc.decode('utf-8').upper()
    data['phone'] = request.vars.phone
    data['mobile'] = request.vars.mobile
    if request.vars.state_id:
        data['state_id'] = request.vars.state_id
    if request.vars.municipality_id:
        data['municipality_id'] = request.vars.municipality_id
    if request.vars.locality_id:
        data['locality_id'] = request.vars.locality_id
    data['address'] = request.vars.address.decode('utf-8').upper()
    data['suburb'] = request.vars.suburb.decode('utf-8').upper()
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


@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def get_client_information():
    id = request.vars.id
    data = dict()

    try:
        query = db.clients.id==id
        left = []
        left.append(db.states.on(db.clients.state_id==db.states.id))
        left.append(db.municipalities.on(
            db.clients.municipality_id==db.municipalities.id))
        left.append(db.localities.on(db.clients.locality_id==db.localities.id))
        row = db(query).select(
            db.clients.ALL, db.states.id, db.states.name,
            db.municipalities.id, db.municipalities.name,
            db.localities.id, db.localities.name, left=left).as_list()
        if row:
            data = row[0]
    except:
        db.rollback()

    if data:
        client = data['clients']
        client['date_added'] = str(client['date_added'])
        client['date_modified'] = str(client['date_modified'])

    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return str(data)


@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def update_client():
    id = request.vars.id
    data = dict()

    data['first_name'] = request.vars.first_name.decode('utf-8').upper()
    data['last_name'] = request.vars.last_name.decode('utf-8').upper()
    data['rfc'] = request.vars.rfc.decode('utf-8').upper()
    data['phone'] = request.vars.phone
    data['mobile'] = request.vars.mobile
    if request.vars.state_id:
        data['state_id'] = request.vars.state_id
    if request.vars.municipality_id:
        data['municipality_id'] = request.vars.municipality_id
    if request.vars.locality_id:
        data['locality_id'] = request.vars.locality_id
    data['address'] = request.vars.address.decode('utf-8').upper()
    data['suburb'] = request.vars.suburb.decode('utf-8').upper()
    data['zip_code'] = request.vars.zip_code

    try:
        result = db(db.clients.id==id).update(**data)
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
        if result == 1:
            db.commit()
            return True
        else:
            db.rollback()
            return ''

