# -*- coding: utf-8 -*-

@auth.requires_login()
def index():
    title = 'Inventarios'
    current = ['menu_inventory']
    return dict(title=title, current=current)