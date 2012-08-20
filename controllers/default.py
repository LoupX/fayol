# -*- coding: utf-8 -*-
from gluon.utils import web2py_uuid
from gluon.tools import Recaptcha


def index():

    tkn = ajax_token()

    form = FORM(
        FIELDSET(
            INPUT(_id="usr", _name='usr', _class='input_usr', _type='text', _placeholder='Usuario', _required='required'),
            INPUT(_id="pwd", _name='pwd',_class='input_pwd', _type='password', _placeholder='Contraseña', _required='required'),
            #Recaptcha(request, CAPTCHA_PUBLIC_KEY, CAPTCHA_PRIVATE_KEY),
            _id='inputs'
        ),
        FIELDSET(
            INPUT(_type='submit', _id='submit', _value='Entrar'),
            INPUT(_type='hidden', _id='tkn', _name='tkn', value='%s' % tkn),
            _id='actions'
        )
    )

    return dict(form=form)

def error404():
    return dict()

def ajax_token():
    tkn = web2py_uuid()
    session.tkn = tkn
    return tkn
