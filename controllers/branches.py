# -*- coding: utf-8 -*-
@auth.requires_login()

#Views
def index():
    title = 'Sucursales / Almacenes'
    current = ['menu_catalogs']
    return dict(title=title,  current=current)
    
    
def branch_office():
    title = 'Sucursales'
    current = ['menu_catalogs', 'sidebar_branches', 'sub_branch_office_read']
    return dict(title=title,  current=current)
    
def new_branch_office():
    title = 'Sucursales'
    current = ['menu_catalogs', 'sidebar_branches', 'sub_branch_office_new']
    return dict(title=title,  current=current)
    
def warehouses():
    title = 'Almacenes'
    current = ['menu_catalogs', 'sidebar_warehouses', 'sub_warehouse_read']
    return dict(title=title,  current=current)
    
def new_warehouse():
    title = 'Almacenes'
    current = ['menu_catalogs', 'sidebar_warehouses', 'sub_warehouse_new']
    return dict(title=title,  current=current)
    
def update_branch_office():
    title = 'Sucursales'
    current = ['menu_catalogs', 'sidebar_branches', 'sub_branch_office_new']
    return dict(title=title,  current=current)

def update_warehouse():
    title = 'Almacenes'
    current = ['menu_catalogs', 'sidebar_warehouses', 'sub_warehouse_new']
    return dict(title=title,  current=current)