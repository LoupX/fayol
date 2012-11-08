# -*- coding: utf-8 -*-
import gluon.contrib.simplejson

#Views

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def index():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_read']
    return dict(title=title, current=current)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def new():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_new']
    return dict(title=title, current=current)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def update():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_read']
    vendor_id = request.vars.id
    sid = request.vars.s
    mid = request.vars.m 
    lid = request.vars.l
    return dict(title=title, current=current, id=vendor_id, sid=sid, mid=mid, lid=lid)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def updatep():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_read']
    return dict(title=title, current=current)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def contact_information():
    title = 'Proveedores'
    return dict(title=title)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def pay_information():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_pay']
    #if request.vars.id:
    #    return dict(title=title, current=current, id=request.vars.id)
    #else:
    return dict(title=title, current=current)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def sales_agents():
    title = 'Agentes de ventas'
    return dict(title=title)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def new_agent():
    title = 'Agentes de ventas'
    return dict(title=title)

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def quickedit():
    return dict()

@auth.requires(auth.has_membership(role='GOD') or
               auth.has_membership(role='Administrador'))
def testing():
    myjson = dict(name='bearcode',state='Yucatan', status='True')
    return gluon.contrib.simplejson.dumps(myjson)









