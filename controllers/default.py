# -*- coding: utf-8 -*-
from gluon.utils import web2py_uuid


def index():
    response.flash = 'bienvenido'
    ck = 'cookie'
    if request.cookies.has_key('my_lng'):
        ck = request.cookies['my_lng'].value

    lng = T.force(ck)
    tkn = ajax_token()

    form = FORM(
        FIELDSET(
            INPUT(_id="usr", _name='usr', _class='input_usr', _type='text', _placeholder=T('User'), _required='required'),
            INPUT(_id="pwd", _name='pwd',_class='input_pwd', _type='password', _placeholder=T('Password'), _required='required'),
            _id='inputs'
        ),
        FIELDSET(
            INPUT(_type='submit', _id='submit', _value=T('Log in')),
            INPUT(_type='hidden', _id='tkn', _name='tkn', value='%s' % tkn),
            _id='actions'
        )
    )

    return dict(form=form,lng=lng)

def error404():
    return dict()

def ajax_token():
    tkn = web2py_uuid()
    session.tkn = tkn
    return tkn

