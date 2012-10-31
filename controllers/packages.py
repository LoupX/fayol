# -*- coding: utf-8 -*-

#Views for Packages
@auth.requires_login()
def index():
    title = 'Paquetes y Servicios'
    current = ['menu_catalogs']
    return dict(title=title,  current=current)

@auth.requires_login()
def new_package():
    title = 'Nuevo Paquete'
    current = ['menu_catalogs']
    return dict(title=title,  current=current)

#Views for Services
@auth.requires_login()
def services():
    title = 'Servicios'
    current = ['menu_catalogs', 'sidebar_services', 'sub_services_read']
    return dict(title=title,  current=current)

@auth.requires_login()
def view_service():
    title = 'Servicios'
    current = ['menu_catalogs', 'sidebar_services', 'sub_services_read']
    return dict(title=title,  current=current)

@auth.requires_login()
def new_service():
    title = 'Servicios'
    current = ['menu_catalogs', 'sidebar_services', 'sub_services_new']
    return dict(title=title,  current=current)

@auth.requires_login()
def update_service():
    title = 'Servicios'
    current = ['menu_catalogs', 'sidebar_services', 'sub_services_read']
    return dict(title=title,  current=current)
    
@auth.requires_login()
def service_prices_list():
    title = 'Servicios'
    current = ['menu_catalogs', 'sidebar_services', 'sub_services_read']
    return dict(title=title,  current=current)
    
@auth.requires_login()
def service_list_quickedit():
    title = 'Servicios'
    id = request.vars.id
    name = ""
    price = ""
    try:
        row = db(db.service_price_lists.id==id).select().first()
        name = row.name
        price = row.price
    except:
        db.rollback()
    current = ['menu_catalogs', 'sidebar_services', 'sub_services_read']
    return dict(title=title, name=name, price=price,  current=current)