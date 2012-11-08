# -*- coding: utf-8 -*-

@auth.requires_membership('GOD', 'Administrador')
def index():
    title = 'Catálogos'
    return dict(title=title)
