# -*- coding: utf-8 -*-
from gluon.tools import Auth

try:
    auth = Auth(db, hmac_key=Auth.get_or_create_key())
    auth.define_tables(username=True)
except:
    raise HTTP(500)
