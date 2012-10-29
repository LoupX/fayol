# -*- coding: utf-8 -*-
@auth.requires_login()

def index():
    title = 'Localidades'
    current = ['menu_catalogs', 'sidebar_localities']
    return dict(title=title, current=current)