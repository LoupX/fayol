# -*- coding: utf-8 -*-

def login():
    """
    Login states (responses):
    0. Not logged in, invalid credentials.
    1. Logged in.
    2. Attempts limit reached. Captcha is now required.
    3. Invalid request.
    """
    valid = False

    #If it's not an ajax request, tell the cliente the page does not exists.
    if not request.ajax:
        attempts(1)
        raise HTTP(404)

    #Validates that the http headers comes from the right server and right method. If not, the request is invalid.
    if  request.env.request_method == 'POST' and HOST == request.env.http_referer:
        valid = True
    else:
        attempts(1)
        return 3

    #Validates the Captcha code.
    if session.attempts and session.attempts >= 4:
        #Captcha stuff
        pass

    if valid:

        #If the login fields are not complete, the request is dumped
        if not request.vars.usr or not request.vars.pwd or not request.vars.tkn:
            attempts(1)
            return 0

        usr = request.vars.usr
        pwd = request.vars.pwd
        tkn = request.vars.tkn

        #Checks the form token. Also checks for a token value in the session in case the token request is deleted from the client side.
        if not session.tkn and tkn != session.tkn:
            attempts(1)
            return 0

        #Checks the password length.
        if len(pwd) < 6:
            attempts(1)
            return 0

        #Check the user credentials
        auth.login_bare(usr, pwd)

        if auth.is_logged_in():
            attempts(0)
            return 1
        else:
            attempts(1)
            return 0

def logout():
    auth.logout()


def attempts(num):
    """
    0 = reset attempts.
    1 = attempts++
    """
    if not session.attempts:
        session.attempts = 0
    elif num == 1:
        session.attempts += 1
        session.forget(tkn)
    elif num == 0:
        session.forget(attempts)
        session.forget(tkn)
