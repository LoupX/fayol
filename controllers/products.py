# -*- coding: utf-8 -*-

@auth.requires_login()
def index():
    title = 'Productos'
    current = ['menu_catalogs', 'sidebar_products', 'sub_products_read']
    return dict(title=title, current=current)

@auth.requires_login()
def new_product():
    title = 'Productos'
    current = ['menu_catalogs', 'sidebar_products', 'sub_products_new']
    return dict(title=title, current=current)

@auth.requires_login()
def view_product():
    title = 'Productos'
    current = ['menu_catalogs', 'sidebar_products', 'sub_products_read']
    return dict(title=title, current=current)

@auth.requires_login()
def prices_list():
    title = 'Productos'
    current = ['menu_catalogs', 'sidebar_products', 'sub_products_prices']
    return dict(title=title, current=current)

@auth.requires_login()
def brands():
    title = 'Marcas'
    current = ['menu_catalogs', 'sidebar_brand', 'sub_brand_read']
    return dict(title=title, current=current)

@auth.requires_login()
def brand_quickedit():
    title = 'Marcas'
    id = request.vars.id
    name = ""
    description = ""
    try:
        row = db.brand_descriptions[id]
        name = row.name
        description = row.description
    except:
        db.rollback()
    return dict(title=title, name=name, description=description)

@auth.requires_login()
def new_brand():
    title = 'Marcas'
    current = ['menu_catalogs', 'sidebar_brand', 'sub_brand_new']
    return dict(title=title, current=current)

@auth.requires_login()
def categories():
    title = 'Categorías'
    current = ['menu_catalogs', 'sidebar_categories', 'sub_categories_read']
    return dict(title=title, current=current)

@auth.requires_login()
def new_category():
    title = 'Categorías'
    current = ['menu_catalogs', 'sidebar_categories', 'sub_categories_new']
    return dict(title=title, current=current)

@auth.requires_login()
def categories_quickedit():
    title = 'Categorías'
    return dict(title=title)

@auth.requires_login()
def units():
    title = 'Unidades de medida'
    current = ['menu_catalogs', 'sidebar_units', 'sub_units_read']
    return dict(title=title, current=current)

@auth.requires_login()
def units_quickedit():
    title = 'Unidades de medida'
    return dict(title=title)

@auth.requires_login()
def new_unit():
    title = 'Unidades de medida'
    current = ['menu_catalogs', 'sidebar_units', 'sub_units_new']
    return dict(title=title,  current=current)
