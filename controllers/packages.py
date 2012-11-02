# -*- coding: utf-8 -*-

#Views for Packages
@auth.requires_login()
def index():
    title = 'Paquetes'
    current = ['menu_catalogs', 'sidebar_packages', 'sub_packages_read']
    session.prev = URL(c='packages', f='index')
    return dict(title=title,  current=current)

@auth.requires_login()
def new_package():
    title = 'Nuevo Paquete'
    current = ['menu_catalogs', 'sidebar_packages', 'sub_packages_new']
    session.prev = URL(c='packages', f='new_package')
    return dict(title=title,  current=current)

@auth.requires_login()
def select_products():
    if session.prev != URL(c='packages', f='new_package'):
        session.prev = None
        redirect(URL(c='packages', f='new_package'))
    session.prev = None
    title = 'Seleccionar productos para agregar al paquete.'
    current = ['menu_catalogs', 'sidebar_packages', 'sub_packages_new']
    return dict(title=title,  current=current)

@auth.requires_login()
def update_select_products():
    valid = [URL(c='packages', f='index'), URL(c='packages', f='view_package')]
    if session.prev not in valid:
        session.prev = None
        redirect(URL(c='packages', f='index'))
    session.prev = None
    title = 'Actualizar productos del paquete.'
    current = ['menu_catalogs', 'sidebar_packages', 'sub_packages_read']
    return dict(title=title,  current=current)

@auth.requires_login()
def view_package():
    title = 'Paquetes'
    current = ['menu_catalogs', 'sidebar_packages', 'sub_packages_read']
    session.prev = URL(c='packages', f='view_package')
    return dict(title=title,  current=current)

@auth.requires_login()
def update_package():
    title = 'Paquetes'
    current = ['menu_catalogs', 'sidebar_packages', 'sub_packages_read']
    return dict(title=title,  current=current)
    
@auth.requires_login()
def package_price_list():
    title = 'Listas de Precios'
    current = ['menu_catalogs', 'sidebar_packages', 'sub_packages_read']
    return dict(title=title,  current=current)
    
@auth.requires_login()
def package_list_quickedit():
    title = 'Paquetes'
    id = request.vars.id
    name = ""
    price = ""
    try:
        row = db(db.package_price_lists.id==id).select().first()
        name = row.name
        price = row.price
    except:
        db.rollback()
    current = ['menu_catalogs', 'sidebar_services', 'sub_services_read']
    return dict(title=title, name=name, price=price,  current=current)

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
