# -*- coding: utf-8 -*-

def index():
    tbl_language= db.language
    form = SQLFORM(tbl_language)
    return dict(form=form)
