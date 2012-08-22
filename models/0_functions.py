# -*- coding: utf-8 -*-

def mail_error(error):
    from gluon.tools import Mail
    mail = Mail()
    mail.settings.server = MAIL_SERVER
    mail.settings.sender = MAIL_SENDER
    mail.settings.login = '{}:{}'.format(MAIL_USER, MAIL_PASSWORD)

    to = [ADMIN_MAIL]
    subject = 'An error ocurred in {}'.format(HOST)
    message = error #Just for semantic reasons.

    sended = mail.send(to, subject, message)
    return sended

def write_error(error):
    from os import path
    from datetime import date
    d = date.today().isoformat()
    fp = path.join(request.folder, 'errors', 'error-{}.log'.format(d))

    try:
        f = open(fp, 'a')
        f.write(error)
        f.write('\n')
        f.close()
        writed = True
    except :
        writed = False

    return writed

def error_handler(error):
    write_error(error)
