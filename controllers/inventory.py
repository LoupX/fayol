# -*- coding: utf-8 -*-

@auth.requires_membership('GOD', 'Almacenista')
def index():
    title = 'Consultar movimientos'
    current = ['menu_inventory', 'sidebar_index']
    return dict(title=title, current=current)
    
@auth.requires_membership('GOD', 'Almacenista')
def entries():
    title = 'Entradas'
    current = ['menu_inventory', 'sidebar_entries']
    return dict(title=title, current=current)

@auth.requires_membership('GOD', 'Almacenista')
def discounts():
    title = 'Salidas'
    current = ['menu_inventory', 'sidebar_discounts']
    return dict(title=title, current=current)

@auth.requires_membership('GOD', 'Almacenista')
def view_transfer():
    title = 'Traspasos'
    current = ['menu_inventory', 'sidebar_view_tranfers']
    return dict(title=title, current=current)
    
@auth.requires_membership('GOD', 'Almacenista')
def tranfers():
    title = 'Traspasos'
    current = ['menu_inventory', 'sidebar_tranfers']
    return dict(title=title, current=current)

@auth.requires_membership('GOD', 'Almacenista')
def transfer_products():
    title = 'Traspasos'
    current = ['menu_inventory', 'sidebar_tranfers']
    return dict(title=title, current=current)

@auth.requires_membership('GOD', 'Almacenista')
def products_entries():
    title = 'Traspasos'
    current = ['menu_inventory', 'sidebar_tranfers']
    return dict(title=title, current=current)  