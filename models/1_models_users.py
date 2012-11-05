# -*- coding: utf-8 -*-
from gluon.tools import Auth

auth = Auth(db, hmac_key=Auth.get_or_create_key())
auth.define_tables(username=True, migrate=MIGRATE)
auth.settings.controller = 'login'
auth.settings.function = 'index'
auth.settings.login_url = URL('login', 'index')
auth.settings.login_next = URL('default', 'index')
auth.settings.logout_next = URL('login', 'index')
auth.settings.login_after_registration = False
