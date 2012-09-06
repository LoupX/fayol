# -*- coding: utf-8 -*-

"""User manual authentication

Responsible for the user authentication via ajax.
"""

from urllib import urlencode
from urllib2 import Request, urlopen


def login():

    """Process the login request and provide one of the following responses defined in the dictionary.

    Login states (responses):
    0. Not logged in, invalid credentials.
    1. Logged in.
    2. Invalid captcha.
    3. Invalid request.
    """

    #Validate request.
    T.force(session.lng)
    responses = [T('Invalid credentials'), T('Logged in'), T('Invalid captcha'), T('Invalid request')]
    if not request.ajax:
        attempts()
        raise HTTP(400)
    if  request.env.request_method != 'POST':
        attempts()
        return responses[3]
    #Validate the Captcha code if any.
    if session.attempts > 3:
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
            if res.read(1) != 't':
                return responses[2]
        else:
            attempts()
            return responses[2]
    #Validate fields and tries to do a login.
    if not request.vars.usr or not request.vars.pwd or not request.vars.tkn:
        attempts()
        return responses[0]
    usr = request.vars.usr
    pwd = request.vars.pwd
    tkn = request.vars.tkn
    if not session.tkn or tkn != session.tkn:
        attempts()
        return responses[0]
    if len(pwd) < 6:
        attempts()
        return responses[0]
    auth.login_bare(usr, pwd)
    if auth.is_logged_in():
        attempts(0)
        redirect(URL('test', 'index'))
    else:
        attempts()
        return responses[0]

def logout():
    auth.logout()

def attempts(code=1):

    """Save the login attempts into the session
    0 = reset attempts.
    1 = attempts++
    """

    if not request.ajax:
        raise HTTP(400)
    if not session.attempts:
        session.attempts = 1
    elif code == 1:
        session.attempts += 1
        session.tkn = None
    elif code == 0:
        session.attempts = None
        session.tkn = None

def check_attempts():

    """Provide the number of attempts to the client."""

    if not request.ajax:
        raise HTTP(400)
    else:
        return session.attempts
