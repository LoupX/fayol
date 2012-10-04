# -*- coding: utf-8 -*-
from gluon.tools import Recaptcha

def index():
    if auth.is_logged_in():
        redirect(URL(c='default'))
    return dict()
