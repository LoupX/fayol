# -*- coding: utf-8 -*-


def index():
	form = FORM(
				FIELDSET(
						INPUT(_id='usr', _type='text', _placeholder='Usuario', _required='required'),
						INPUT(_id='pwd', _type='password', _placeholder='Contraseña', _required='required')
				,_id='inputs'),
				FIELDSET(
						INPUT(_type='submit', _id='submit', _value='Entrar')
				,_id='actions')
			)

	if form.accepts(request,session):
		response.flash = 'form accepted'
	return dict(form=form)

def data():
	return '0'

