# -*- coding: utf-8 -*-

#Views
def index():
    title = 'Productos'
    return dict(title=title)
    
def new_product():
	title = 'Productos'
	return dict(title=title)
    
def categories():
    title = 'Categorías'
    return dict(title=title)
     
def trademarks():
    title = 'Marcas'
    return dict(title=title)
    
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
    

	
