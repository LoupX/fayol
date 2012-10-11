# -*- coding: utf-8 -*-
import gluon.contrib.simplejson

#Views
def index():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_read']
    vendors = get_vendors()
    vendor_info = get_vendor_info()
    return dict(title=title, current=current, vendors=vendors, **vendor_info)

def new():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_new']
    return dict(title=title, current=current)

def update():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_read']
    vendor_id = None
    if request.vars.id:
        try:
            vendor_id = int(request.vars.id)
            session.vendor_id = vendor_id
        except:
            redirect(URL(c='vendors', f='new'))
    else:
        redirect(URL(c='vendors', f='new'))
    row = db(db.vendors.id==vendor_id).select().as_list()
    if not row:
        redirect(URL(c='vendors', f='new'))
    else:
        row = row[0]

    options = [OPTION('Seleccionar', _value='')]
    states = read_states()
    if states:
        for s in states:
            if s['id']==row['state_id']:
                options += [OPTION(s['name'], _value=s['id'],
                    _selected='selected')]
            else:
                options += [OPTION(s['name'], _value=s['id'])]
    states = SELECT(_name='state', _id='state', *options)

    options = [OPTION('Seleccionar', _value='')]
    municipalities = read_municipalities(row['state_id'])
    if municipalities:
        for m in municipalities:
            if m['id']==row['municipality_id']:
                options += [OPTION(m['name'], _value=m['id'],
                    _selected='selected')]
            else:
                options += [OPTION(m['name'], _value=m['id'])]
    municipalities = SELECT(_name='municipality', _id='municipality', *options)

    options = [OPTION('Seleccionar', _value='')]
    localities = read_localities(row['municipality_id'])
    if localities:
        for l in localities:
            if l['id']==row['locality_id']:
                options += [OPTION(l['name'], _value=l['id'],
                    _selected='selected')]
            else:
                options += [OPTION(l['name'], _value=l['id'])]
    localities = SELECT(_name='locality', _id='locality', *options)

    return dict(title=title, current=current, states=states,
        municipalities=municipalities, localities=localities, **row)

def contact_information():
    title = 'Proveedores'
    return dict(title=title)

def pay_information():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_pay']
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









