# -*- coding: utf-8 -*-

@auth.requires_login()
def index():
    title = 'Usuarios'
    current = ['menu_users', 'sidebar_users', 'sub_users_read']
    return dict(title=title, current=current)
    
@auth.requires_login()
def new_user():
    title = 'Usuarios'
    current = ['menu_users', 'sidebar_users', 'sub_users_new']
    return dict(title=title, current=current)