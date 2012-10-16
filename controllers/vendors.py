# -*- coding: utf-8 -*-
@auth.requires_login()
import gluon.contrib.simplejson

#Views
def index():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_read']
    return dict(title=title, current=current)

def new():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_new']
    return dict(title=title, current=current)

def update():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_read']
    vendor_id = request.vars.id
    sid = request.vars.s
    mid = request.vars.m 
    lid = request.vars.l
    return dict(title=title, current=current, id=vendor_id, sid=sid, mid=mid, lid=lid)

def updatep():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_read']
    return dict(title=title, current=current)

def contact_information():
    title = 'Proveedores'
    return dict(title=title)

def pay_information():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_pay']
    #if request.vars.id:
    #    return dict(title=title, current=current, id=request.vars.id)
    #else:
    return dict(title=title, current=current)

def sales_agents():
    title = 'Agentes de ventas'
    return dict(title=title)

def new_agent():
    title = 'Agentes de ventas'
    return dict(title=title)

def quickedit():
    return dict()

def testing():
    myjson = dict(name='bearcode',state='Yucatan', status='True')
    return gluon.contrib.simplejson.dumps(myjson)









