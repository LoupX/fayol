# -*- coding: utf-8 -*-

@auth.requires(auth.has_membership(role='GOD'))
def index():
    title = 'Usuarios'
    current = ['menu_users', 'sidebar_users', 'sub_users_read']
    return dict(title=title, current=current)

@auth.requires(auth.has_membership(role='GOD'))
def new_user():
    title = 'Usuarios'
    current = ['menu_users', 'sidebar_users', 'sub_users_new']
    return dict(title=title, current=current)

@auth.requires(auth.has_membership(role='GOD'))
def update_user():
    title = 'Usuarios'
    current = ['menu_users', 'sidebar_users', 'sub_users_read']
    return dict(title=title, current=current)

def update_password():
    title = 'Contraseña'
    current = ['menu_users', 'sidebar_users', 'sub_users_read']
    return dict(title=title, current=current)

