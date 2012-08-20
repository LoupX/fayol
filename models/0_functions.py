# -*- coding: utf-8 -*-

def send_error(error):
    from gluon.tools import Mail
    mail = Mail()
    mail.settings.server = MAIL_SERVER
    mail.settings.sender = MAIL_SENDER
    mail.settings.login = '{}:{}'.format(MAIL_USER, MAIL_PASSWORD)

    to = [ADMIN_MAIL]
    subject = 'An error ocurred in {}'.format(HOST)
    message = error

    if not mail.send(to, subject, message):
        pass
