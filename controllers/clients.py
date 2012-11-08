# -*- coding: utf-8 -*-

@auth.requires_membership('GOD')
def index():
    title = 'Clientes'
    current = ['menu_catalogs', 'sidebar_clients', 'sub_clients_read']
    return dict(title=title, current=current)
    
@auth.requires_membership('GOD')
def new_client():
    title = 'Clientes'
    current = ['menu_catalogs', 'sidebar_clients', 'sub_clients_new']
    return dict(title=title, current=current)