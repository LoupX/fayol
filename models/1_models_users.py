# -*- coding: utf-8 -*-
from gluon.tools import Auth

auth = Auth(db)
auth.settings.extra_fields['auth_user'] = [
    Field('address', 'string'),
    Field('country_id', 'reference countries', default=1),
    Field('state_id', 'reference states'),
    Field('municipality_id', 'reference municipalities'),
    Field('locality_id', 'reference localities'),
    Field('birthday', 'date'),
    Field('social_secure_number', 'string', length=11),
    Field('salary', 'decimal(12,2)'),
    Field('zip_code', 'string', length=5),
    Field('phone', 'string', length=10),
    Field('mobile', 'string', length=10)]
auth.define_tables(username=True, migrate=MIGRATE)
auth.settings.controller = 'login'
auth.settings.function = 'index'
auth.settings.login_url = URL('login', 'index')
auth.settings.login_next = URL('default', 'index')
auth.settings.logout_next = URL('login', 'index')
auth.settings.login_after_registration = False
auth.settings.expiration = 18000


try:
    if db(db.auth_group).isempty():
        god_group_id = auth.add_group('GOD', 'Administrador del sistema')
        auth.add_group('Administrador', 'Administrador local')
        auth.add_group('Gerente', 'Gerente de sucursal')
        auth.add_group('Vendedor de mostrador', 'Vendedor de mostrador'),
        auth.add_group('Almacenista', 'Encargado de almacen')
        auth.add_group('Cajero', '')
    else:
        god_group_id = db(db.auth_group.role=='GOD').select().first()
        god_group_id = god_group_id.id

    if db(db.auth_user).isempty():
        password = db.auth_user.password.validate('qazWSX11')[0]
        data = dict()
        data['first_name'] = 'Yisus'
        data['last_name'] = 'Craist'
        data['username'] = 'god'
        data['password'] = password
        data['email'] = 'jd@beardcode.mx'
        god_user_id = db.auth_user.insert(**data)
        auth.add_membership(god_group_id, god_user_id)
except:
    db.rollback()
    raise HTTP(503)
else:
    db.commit()
