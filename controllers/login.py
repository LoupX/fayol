# -*- coding: utf-8 -*-
from gluon.utils import web2py_uuid
from gluon.tools import Recaptcha


def index():

    if auth.is_logged_in():
        redirect(URL(c='dashboard'))

    session.lng = T.accepted_language or 'es-mx'
    if request.cookies.has_key('my_lng'):
        session.lng = request.cookies['my_lng'].value
        T.force(session.lng)
    else:
        T.force(session.lng)

    tkn = ajax_token()

    form = FORM(
        FIELDSET(
            INPUT(_id="usr", _name='usr', _class='input_usr', _type='text', _placeholder=T('User'), _required='required'),
            INPUT(_id="pwd", _name='pwd',_class='input_pwd', _type='password', _placeholder=T('Password'), _required='required'),
            DIV(Recaptcha(request, CAPTCHA_PUBLIC_KEY, CAPTCHA_PRIVATE_KEY), _class='captcha'),
            _id='inputs'
        ),
        FIELDSET(
            INPUT(_type='submit', _id='submit', _value=T('Log in')),
            INPUT(_type='hidden', _id='tkn', _name='tkn', value='%s' % tkn),
            _id='actions'
        )
    )

    return dict(form=form)

def error404():
    T.force(session.lng)
    return dict()

def error400():
    T.force(session.lng)
    return dict()

def error500():
    T.force(session.lng)
    return dict()

def error503():
    T.force(session.lng)
    return dict()

def ajax_token():
    tkn = web2py_uuid()
    session.tkn = tkn
    return tkn
