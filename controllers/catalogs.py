# -*- coding: utf-8 -*-
@auth.requires_login()

def index():
    title = 'Catálogos'
    return dict(title=title)
