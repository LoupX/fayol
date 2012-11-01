# -*- coding: utf-8 -*-

def test():
    login = auth.login_bare('root', '12345678')
    return str(login)


def login_bare(self, username, password):
    """
    logins user as specified by usernname (or email) and password
    """
    request = current.request
    session = current.session
    table_user = self.table_user()
    if self.settings.login_userfield:
        userfield = self.settings.login_userfield
    elif 'username' in table_user.fields:
        userfield = 'username'
    else:
        userfield = 'email'
    passfield = self.settings.password_field
    user = self.db(table_user[userfield] == username).select().first()
    if user and user.get(passfield, False):
        password = table_user[passfield].validate(password)[0]
        if not user.registration_key and password == user[passfield]:
            self.login_user(user)
            return user
    else:
        # user not in database try other login methods
        for login_method in self.settings.login_methods:
            if login_method != self and login_method(username, password):
                self.user = username
                return username
    return False
