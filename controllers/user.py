# -*- coding: utf-8 -*-
from urllib import urlencode
from urllib2 import Request, urlopen
def login():
    """
    Login states (responses):
    0. Not logged in, invalid credentials.
    1. Logged in.
    2. Invalid captcha.
    3. Invalid request.
    """
    valid = False

    #If it's not an ajax request, tell the cliente the page does not exists.
    if not request.ajax:
        attempts()
        raise HTTP(404)

    #Validates that the http headers comes from the right server and right method. If not, the request is invalid.
    #It only does it when debug = False
    if DEBUG:
        if  request.env.request_method == 'POST':
            valid = True
        else:
            attempts()
            return 3
    else:
        if  request.env.request_method == 'POST' and HOST == request.env.http_referer:
            valid = True
        else:
            attempts()
            return 3

    #Validates the Captcha code.
    if session.attempts and session.attempts >= 0:
        if request.vars.r_challenge and request.vars.r_response:
            values = {
                     'privatekey':CAPTCHA_PRIVATE_KEY,
                     'remoteip':request.env.remote_addr,
                     'challenge':request.vars.r_challenge,
                     'response':request.vars.r_response
            }
            data = urlencode(values)
            req = Request(
                CAPTCHA_URL,
                data
            )
            res = urlopen(req)
            if res.read(1) == 't':
                return 'successful captcha'
            else:
                return 2
        else:
            attempts()
            return 2

    if valid:

        #If the login fields are not complete, the request is dumped
        if not request.vars.usr or not request.vars.pwd or not request.vars.tkn:
            attempts()
            return 0

        usr = request.vars.usr
        pwd = request.vars.pwd
        tkn = request.vars.tkn

        #Checks the form token. Also checks for a token value in the session in case the token request is deleted from the client side.
        if not session.tkn and tkn != session.tkn:
            attempts()
            return 0

        #Checks the password length.
        if len(pwd) < 6:
            attempts()
            return 0

        #Check the user credentials
        auth.login_bare(usr, pwd)

        if auth.is_logged_in():
            attempts(0)
            return 1
        else:
            attempts()
            return 0

def logout():
    auth.logout()


def attempts(code=1):
    """
    0 = reset attempts.
    1 = attempts++
    """
    if not session.attempts:
        session.attempts = 1
    elif code == 1:
        session.attempts += 1
        session.tkn = None
    elif code == 0:
        session.attempts = None
        session.tkn = None
