# -*- coding: utf-8 -*-

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Almacenista'))
def index():
    title = 'Consultar movimientos'
    current = ['menu_inventory', 'sidebar_index']
    return dict(title=title, current=current)
    
@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Almacenista'))
def entries():
    title = 'Entradas'
    current = ['menu_inventory', 'sidebar_entries']
    return dict(title=title, current=current)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Almacenista'))
def discounts():
    title = 'Salidas'
    current = ['menu_inventory', 'sidebar_discounts']
    return dict(title=title, current=current)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Almacenista'))
def view_transfer():
    title = 'Traspasos'
    current = ['menu_inventory', 'sidebar_view_tranfers']
    return dict(title=title, current=current)
    
@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Almacenista'))
def tranfers():
    title = 'Traspasos'
    current = ['menu_inventory', 'sidebar_tranfers']
    return dict(title=title, current=current)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Almacenista'))
def transfer_products():
    title = 'Traspasos'
    current = ['menu_inventory', 'sidebar_tranfers']
    return dict(title=title, current=current)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Almacenista'))
def products_entries():
    title = 'Traspasos'
    current = ['menu_inventory', 'sidebar_tranfers']
    return dict(title=title, current=current)  