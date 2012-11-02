# -*- coding: utf-8 -*-

def test():
    session.forget()
    login = auth.login_bare('test', '12345678')
    return '{} {}'.format(login.first_name, login.last_name)

