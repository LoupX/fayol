# -*- coding: utf-8 -*-

@auth.requires_membership('GOD', 'Administrador')
def index():
    title = 'Productos'
    current = ['menu_catalogs', 'sidebar_products', 'sub_products_read']
    return dict(title=title, current=current)

@auth.requires_membership('GOD', 'Administrador')
def new_product():
    title = 'Productos'
    current = ['menu_catalogs', 'sidebar_products', 'sub_products_new']
    return dict(title=title, current=current)

@auth.requires_membership('GOD', 'Administrador')
def view_product():
    title = 'Productos'
    current = ['menu_catalogs', 'sidebar_products', 'sub_products_read']
    return dict(title=title, current=current)
    
@auth.requires_membership('GOD', 'Administrador')
def update_product():
    row = None
    try:
        row = db.products[request.vars.id]
    except:
        db.rollback()
    if not row:
        redirect(URL(c='products', f='index'))
    title = 'Productos'
    current = ['menu_catalogs', 'sidebar_products', 'sub_products_read']
    return dict(title=title, current=current)

@auth.requires_membership('GOD', 'Administrador')
def prices_list():
    title = 'Lista de Precios'
    current = ['menu_catalogs', 'sidebar_products', 'sub_products_read']
    return dict(title=title, current=current)

@auth.requires_membership('GOD', 'Administrador')
def list_quickedit():
    title = 'Productos'
    id = request.vars.id
    name = ""
    price = ""
    try:
        row = db(db.product_price_lists.id==id).select().first()
        name = row.name
        price = row.price
    except:
        db.rollback()
    return dict(title=title, name=name, price=price)

@auth.requires_membership('GOD', 'Administrador')
def brands():
    title = 'Marcas'
    current = ['menu_catalogs', 'sidebar_brand', 'sub_brand_read']
    return dict(title=title, current=current)

@auth.requires_membership('GOD', 'Administrador')
def brand_quickedit():
    title = 'Marcas'
    id = request.vars.id
    name = ""
    description = ""
    try:
        row = db(db.brand_descriptions.brand_id==id).select().first()
        name = row.name
        description = row.description
    except:
        db.rollback()
    return dict(title=title, name=name, description=description)

@auth.requires_membership('GOD', 'Administrador')
def new_brand():
    title = 'Marcas'
    current = ['menu_catalogs', 'sidebar_brand', 'sub_brand_new']
    return dict(title=title, current=current)

@auth.requires_membership('GOD', 'Administrador')
def categories():
    title = 'Categorías'
    current = ['menu_catalogs', 'sidebar_categories', 'sub_categories_read']
    return dict(title=title, current=current)

@auth.requires_membership('GOD', 'Administrador')
def new_category():
    title = 'Categorías'
    current = ['menu_catalogs', 'sidebar_categories', 'sub_categories_new']
    return dict(title=title, current=current)

@auth.requires_membership('GOD', 'Administrador')
def categories_quickedit():
    title = 'Categorías'
    id = request.vars.id
    name = ""
    description = ""
    try:
        row = db(db.category_descriptions.category_id==id).select().first()
        name = row.name
        description = row.description
    except:
        db.rollback()
    return dict(title=title, name=name, description=description)

@auth.requires_membership('GOD', 'Administrador')
def units():
    title = 'Unidades de medida'
    current = ['menu_catalogs', 'sidebar_units', 'sub_units_read']
    return dict(title=title, current=current)

@auth.requires_membership('GOD', 'Administrador')
def units_quickedit():
    title = 'Unidades de medida'
    id = request.vars.id
    name = ""
    abbreviation = ""
    try:
        row = db.units[id]
        name = row.name
        abbreviation = row.abbreviation
    except:
        db.rollback()
    return dict(title=title, name=name, abbreviation=abbreviation)

@auth.requires_membership('GOD', 'Administrador')
def new_unit():
    title = 'Unidades de medida'
    current = ['menu_catalogs', 'sidebar_units', 'sub_units_new']
    return dict(title=title,  current=current)
