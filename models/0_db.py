# -*- coding: utf-8 -*-

try:
    db = DAL('postgres://%(user)s:%(pwd)s@%(host)s:%(port)i/%(db)s' %
             dict(user=DB_USER, pwd = DB_PASS, host=DB_HOST, port=DB_PORT,
                 db=DB))
except Exception as e:
    raise HTTP(503)

try:
    sqlite = DAL('sqlite://dictionaries.db')
except Exception as e:
    pass
