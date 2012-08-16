# -*- coding: utf-8 -*-
from gluon.tools import Auth

auth = Auth(db, hmac_key=Auth.get_or_create_key())
auth.define_tables(username=True, migrate=False)
