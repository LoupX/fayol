# -*- coding: utf-8 -*-

"""User manual authentication

Responsible for the user authentication via ajax.
"""

from urllib import urlencode
from urllib2 import Request, urlopen
from gluon.utils import web2py_uuid

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
    """
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
    """
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
        return 'true'
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

def ajax_token():
    tkn = web2py_uuid()
    session.tkn = tkn
    return tkn

@auth.requires_login()
def check_user():
    usr = request.vars.usr
    pwd = request.vars.pwd
    if not usr or not pwd:
        return ''
    user = db(db.auth_user.username == usr).select().first()
    if user and user.get('password', False):
        password = db.auth_user.password.validate(pwd)[0]
        if not user.registration_key and password == user['password']:
            session.selected_user = user
            return True
        else:
            return ''

@auth.requires_login()
def create_user():
    data = dict()
    id = None

    pwd = request.vars.password
    data['password'] = db.auth_user.password.validate(pwd)[0]
    data['username'] = request.vars.username
    data['address'] = request.vars.address
    if request.vars.state_id:
        data['state_id'] = request.vars.state_id
    if request.vars.municipality_id:
        data['municipality_id'] = request.vars.municipality_id
    if request.vars.locality_id:
        data['locality_id'] = request.vars.locality_id
    data['birthday'] = request.vars.birthday
    data['social_secure_number'] = request.vars.social_secure_number
    data['salary'] = request.vars.salary
    data['zip_code'] = request.vars.zip_code
    data['phone'] = request.vars.phone
    data['mobile'] = request.vars.mobile

    try:
        id = db.auth_user.insert(**data)
    except:
        db.rollback()
        return ''
    else:
        db.commit()
        return id

@auth.requires_login()
def update_user():
    data = dict()
    id = request.vars.id

    pwd = request.vars.password
    data['password'] = db.auth_user.password.validate(pwd)[0]
    data['username'] = request.vars.username
    data['address'] = request.vars.address
    if request.vars.state_id:
        data['state_id'] = request.vars.state_id
    if request.vars.municipality_id:
        data['municipality_id'] = request.vars.municipality_id
    if request.vars.locality_id:
        data['locality_id'] = request.vars.locality_id
    data['birthday'] = request.vars.birthday
    data['social_secure_number'] = request.vars.social_secure_number
    data['salary'] = request.vars.salary
    data['zip_code'] = request.vars.zip_code
    data['phone'] = request.vars.phone
    data['mobile'] = request.vars.mobile

@auth.requires_login()
def get_groups():
    data = dict()
    try:
        data = db(db.auth_group).select().as_list()
    except:
        db.rollback()
    from gluon.contrib import simplejson
    data = simplejson.dumps(data)
    return str(data)
