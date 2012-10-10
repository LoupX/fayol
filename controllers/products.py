# -*- coding: utf-8 -*-

#Views
def index():
    title = 'Productos'
    return dict(title=title)
    
def new_product():
	title = 'Productos'
	return dict(title=title)
	     
def trademarks():
    title = 'Marcas'
    current = ['menu_catalogs', 'sidebar_trademark', 'sub_trademark_read']
    return dict(title=title, current=current)
    
def trademark_quickedit():
	title = 'Marcas'
	return dict(title=title)

def new_trademark():
	title = 'Marcas'
	current = ['menu_catalogs', 'sidebar_trademark', 'sub_trademark_new']
	return dict(title=title, current=current)    
    
def categories():
    title = 'Categorías'
    current = ['menu_catalogs', 'sidebar_categories', 'sub_categories_read']
    return dict(title=title, current=current)
    
def categories_quickedit():
	title = 'Unidades de medida'
	return dict(title=title)
    
def new_category():
	title = 'Categorías'
	current = ['menu_catalogs', 'sidebar_categories', 'sub_categories_new']
	return dict(title=title, current=current)
    
def units():
    title = 'Unidades de medida'
    current = ['menu_catalogs', 'sidebar_units', 'sub_units_read']
    return dict(title=title, current=current)

def units_quickedit():
	title = 'Unidades de medida'
	return dict(title=title)
	
def new_unit():
    title = 'Unidades de medida'
    current = ['menu_catalogs', 'sidebar_units', 'sub_units_new']
    return dict(title=title,  current=current)