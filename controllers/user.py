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
    responses = [T('Invalid credentials'), T('Logged in'), T('Invalid captcha'), T('Invalid request')]

    if not request.ajax:
        attempts()
        error = T('The following address tried to acces the system via with no ajax: {}'.format(request.env.remote_addr))
        send_error(error)
        raise HTTP(400)

    if  request.env.request_method != 'POST':
        attempts()
        return responses[3]

    #Validates the Captcha code.
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
            try:
                res = urlopen(req)
                if res.read(1) != 't':
                    return responses[2]
            except Exception as e:
                error = T('The captcha server may be down :[\n'.format(e))
                send_error(e)
        else:
            attempts()
            return responses[2]

    #If the login fields are not complete, the request is dumped
    if not request.vars.usr or not request.vars.pwd or not request.vars.tkn:
        attempts()
        return responses[0]

    usr = request.vars.usr
    pwd = request.vars.pwd
    tkn = request.vars.tkn

    #Checks the form token. Also checks for a token value in the session in case the token request is deleted from the client side.
    if not session.tkn or tkn != session.tkn:
        attempts()
        return responses[0]

    if len(pwd) < 6:
        attempts()
        return responses[0]

    auth.login_bare(usr, pwd)

    if auth.is_logged_in():
        attempts(0)
        return responses[1]
    else:
        attempts()
        return responses[0]

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

def check_attempts():
    if not request.ajax:
        error = 'We\'ve got a bad voy trying to check attempts without ajax\nIP: {}'.format(request.env.remote_addr)
        send_error(error)
        raise HTTP(400)
    else:
        return session.attempts
