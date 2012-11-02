# -*- coding: utf-8 -*-

@auth.requires_login()
def index():
    title = 'Consultar movimientos'
    current = ['menu_inventory', 'sidebar_index']
    return dict(title=title, current=current)
    
@auth.requires_login()
def entries():
    title = 'Entradas'
    current = ['menu_inventory', 'sidebar_entries']
    return dict(title=title, current=current)

@auth.requires_login()
def discounts():
    title = 'Salidas'
    current = ['menu_inventory', 'sidebar_discounts']
    return dict(title=title, current=current)
    
@auth.requires_login()
def tranfers():
    title = 'Traspasos'
    current = ['menu_inventory', 'sidebar_tranfers']
    return dict(title=title, current=current)

@auth.requires_login()
def products_entries():
    title = 'Traspasos'
    current = ['menu_inventory', 'sidebar_tranfers']
    return dict(title=title, current=current)  