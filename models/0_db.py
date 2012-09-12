try:
    db = DAL('postgres://%(user)s:%(pwd)s@%(host)s:%(port)i/%(db)s' % dict(user=DB_USER, pwd = DB_PASS, host=DB_HOST, port=DB_PORT, db=DB))
except Exception as e:
    raise HTTP(503)

from gluon.tools import Auth
auth = Auth(db, hmac_key=Auth.get_or_create_key())
