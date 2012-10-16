# -*- coding: utf-8 -*-
import gluon.contrib.simplejson

#Views
@auth.requires_login()
def index():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_read']
    return dict(title=title, current=current)

@auth.requires_login()
def new():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_new']
    return dict(title=title, current=current)

@auth.requires_login()
def update():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_read']
    vendor_id = request.vars.id
    sid = request.vars.s
    mid = request.vars.m 
    lid = request.vars.l
    return dict(title=title, current=current, id=vendor_id, sid=sid, mid=mid, lid=lid)

@auth.requires_login()
def updatep():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_read']
    return dict(title=title, current=current)

@auth.requires_login()
def contact_information():
    title = 'Proveedores'
    return dict(title=title)

@auth.requires_login()
def pay_information():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_pay']
    #if request.vars.id:
    #    return dict(title=title, current=current, id=request.vars.id)
    #else:
    return dict(title=title, current=current)

@auth.requires_login()
def sales_agents():
    title = 'Agentes de ventas'
    return dict(title=title)

@auth.requires_login()
def new_agent():
    title = 'Agentes de ventas'
    return dict(title=title)

@auth.requires_login()
def quickedit():
    return dict()

@auth.requires_login()
def testing():
    myjson = dict(name='bearcode',state='Yucatan', status='True')
    return gluon.contrib.simplejson.dumps(myjson)









