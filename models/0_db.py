try:
    db = DAL('postgres://%(user)s:%(pwd)s@%(host)s:%(port)i/%(db)s' % dict(user=DB_USER, pwd = DB_PASS, host=DB_HOST, port=DB_PORT, db=DB))
except Exception as e:
    send_error(e)
    raise HTTP(503, e)
