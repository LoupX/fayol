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
    title = 'shit'
    current = ['menu_catalogs']
    return dict(title=title,  current=current)

@auth.requires_login()
def new_service():
    title = 'Nuevo Servicio'
    current = ['menu_catalogs']
    return dict(title=title,  current=current)