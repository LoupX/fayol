# -*- coding: utf-8 -*-

def index():
    form = SQLFORM(db.language)
    return dict(form=form)

def error():
    return dict()

