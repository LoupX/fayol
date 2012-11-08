# -*- coding: utf-8 -*-

#Views
@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def index():
    title = 'Sucursales / Almacenes'
    current = ['menu_catalogs']
    return dict(title=title,  current=current)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def branch_office():
    title = 'Sucursales'
    current = ['menu_catalogs', 'sidebar_branches', 'sub_branch_office_read']
    return dict(title=title,  current=current)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def new_branch_office():
    title = 'Sucursales'
    current = ['menu_catalogs', 'sidebar_branches', 'sub_branch_office_new']
    return dict(title=title,  current=current)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def warehouses():
    title = 'Almacenes'
    current = ['menu_catalogs', 'sidebar_warehouses', 'sub_warehouse_read']
    return dict(title=title,  current=current)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def new_warehouse():
    title = 'Almacenes'
    current = ['menu_catalogs', 'sidebar_warehouses', 'sub_warehouse_new']
    return dict(title=title,  current=current)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def update_branch_office():
    title = 'Sucursales'
    current = ['menu_catalogs', 'sidebar_branches', 'sub_branch_office_read']
    sid = request.vars.s
    mid = request.vars.m 
    lid = request.vars.l
    return dict(title=title,  current=current, sid=sid, mid=mid, lid=lid)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def update_warehouse():
    title = 'Almacenes'
    current = ['menu_catalogs', 'sidebar_warehouses', 'sub_warehouse_read']
    sid = request.vars.s
    mid = request.vars.m 
    lid = request.vars.l
    return dict(title=title,  current=current, sid=sid, mid=mid, lid=lid)
