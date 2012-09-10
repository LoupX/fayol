#@auth.requires_login()
nombre       = 'Emir Salazar'
nombre_vista = ''

def index():
    dum          = 'Aqui va las apps'
    dum1         = 'notificaciones'
    nombre_vista = 'Dashboard'
    return dict(dum=dum,dum1=dum1,nombre=nombre,nombre_vista=nombre_vista)

def provedores():
    nombre_vista = 'Proveedores'

    form = FORM(
                DIV(
                    UL(
                        LI(
                            H4('Detalles del Proveedor'),BR(),
                            'Codigo del proveedor: ',INPUT(_class='iptn', _name='codigo', _placeholder='4 digitos', _maxlength='4', requires=[IS_NOT_EMPTY(), IS_LENGTH(maxsize=4), IS_INT_IN_RANGE(0, 10000)] ),BR(),BR(),
                            'Nombre de la Empresa: ',INPUT(_class="iptn", _name="empresa", requires=IS_NOT_EMPTY()),BR(),BR(),
                            'Direccion: ',INPUT(_class="iptn", _name="direccion", requires=IS_NOT_EMPTY()),BR(),BR(),
                            'Ciudad: ',INPUT(_class='iptn', _name='ciudad', requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),BR(),BR(),
                            'Municipio: ',INPUT(_class='iptn', _name='municipio', requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()]),BR(),BR(),
                            'Estado: ',INPUT(_class='iptn', _name='estado', requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC()] ),BR(),BR(),
                            'Codigo Postal: ',INPUT(_class='iptn', _name='cp', _placeholder='5 digitos', _maxlength='5', requires=[IS_NOT_EMPTY(), IS_MATCH('^([1-9]{2}|[0-9][1-9]|[1-9][0-9])[0-9]{3}$')] ),BR(),BR(),
                            'RFC: ',INPUT(_class='iptn', _name='rfc', _placeholder='Ejemplo: XXXXXXXXXX-XX', _maxlength='14', requires=[IS_NOT_EMPTY(), IS_MATCH('^[a-zA-Z]{3,4}(\d{6})(-(\D|\d){3})?$'), IS_LENGTH(maxsize=14,minsize=10)] ),BR(),BR(),
                            'Telefono del Proveedor: ',INPUT(_class='iptn', _name='telp', _placeholder='Ejemplo: 000-0000000',  _maxlength='11', requires=[IS_NOT_EMPTY(), IS_MATCH('^[0-9]{3}-[0-9]{7}$'), IS_LENGTH(maxsize=11)] ),BR(),BR(),
                            'Correo del Proveedor: ',INPUT(_class='iptn', _name='correop', _placeholder='ejemplo@mail.com', requires=IS_EMAIL() ),BR(),BR(),
                            'Pagina web: ',INPUT(_class='iptn', _name='sitio', _placeholder='www.ejemplo.com', requires=IS_URL() ),BR(),BR(),
                        _id='0'),
                        LI(H4('Datos de Contacto'),BR(),
                            'Nombre de Contacto: ',INPUT(_class='iptn', _name='nombre', requires=IS_NOT_EMPTY()),BR(),BR(),
                            'Telefono: ',INPUT(_class='iptn', _name='telefono', _placeholder='Ejemplo: 000-0000000', _maxlength='11', requires=[IS_NOT_EMPTY(), IS_MATCH('^[0-9]{3}-[0-9]{7}$'), IS_LENGTH(maxsize=11)] ),BR(),BR(),
                            'Correo electronico: ',INPUT(_class='iptn', _name='correo', _placeholder='ejemplo@mail.com', requires=IS_EMAIL() ),
                        _id='620'),
                        LI(H4('Formas de pago'),BR(),
                            H5('Cheques'),
                            'Numero de cuenta: ',INPUT(_class='iptn', _name='cuenta', _maxlength='11', requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC(), IS_LENGTH(maxsize=11,minsize=11)]),BR(),BR(),
                            'Banco: ',INPUT(_class='iptn', _name='banco', requires=IS_NOT_EMPTY()),BR(),BR(),BR(),
                            H5('Transferencia'),
                            'CLABE interbancaria:',INPUT(_class='iptn', _name='clabe', _maxlength='18', requires=[IS_NOT_EMPTY(), IS_ALPHANUMERIC(), IS_LENGTH(maxsize=18,minsize=18)] ),BR(),BR(),
                            INPUT(_type='submit', _id='btng', _name='btng', _value='Guardar'),
                        _id='1240')
                    ),
                _class='main_content'),
            _id='form_pro')

    if form.accepts(request,session):
        response.flash = 'Se ha guardado correctamente.'
    elif form.errors:
        response.flash = 'Se encontraron errores. '
    return dict(nombre=nombre,nombre_vista=nombre_vista,form=form)

def productos():
    nombre_vista = 'Productos'
    form = FORM(
        UL(
            LI('Codigo: ',
                INPUT( _class="iptn", _name="prod_codigo", requires=IS_NOT_EMPTY())
            ),
            LI('Nombre: ',
                INPUT( _class="iptn", _name="prod_nombre", requires=IS_NOT_EMPTY())
            ),
            LI('Estado: ',
                INPUT( _class="iptn", _name="prod_estado", _type="radio", _value='1', _id='a', requires=IS_NOT_EMPTY()),LABEL('Activar', _for='a'),
                INPUT( _class="iptn", _name="prod_estado", _type="radio", _value='0', _id='d', requires=IS_NOT_EMPTY()),LABEL('Desactivar', _for='d')
            ),
            LI('Unidad de Medida: ',
                INPUT(_class="iptn", _name="prod_medida", requires=IS_NOT_EMPTY())
            ),
            LI('Nombre Alternativo: ',
                INPUT(_class="iptn", _name="prod_nombre_alt", requires=IS_NOT_EMPTY())
            ),
            LI('Marca: ',
                INPUT(_class="iptn", _name="prod_marca", requires=IS_NOT_EMPTY())
            ),
            LI('Modelo: ',
                INPUT(_class="iptn", _name="prod_modelo", requires=IS_NOT_EMPTY())
            ),
            LI('Codigo Alternativo: ',
                INPUT(_class="iptn", _name="prod_codigo_alt", requires=IS_NOT_EMPTY())
            ),
            LI('Numero de parte: ',
                INPUT(_class="iptn", _name="prod_nparte", requires=IS_NOT_EMPTY())
            ),
            LI('Numero de serie: ',
                INPUT(_class="iptn", _name="prod_nserie", requires=IS_NOT_EMPTY())
            ),
            LI('Descripcion: ',
                INPUT(_class="iptn", _name="prod_descripcion", requires=IS_NOT_EMPTY())
            ),
            LI('Categorias: ',
                SELECT('a', 'b', _class="iptn", _name="prod_categorias", requires=IS_NOT_EMPTY())
            ),
            LI('Proveedor: ',
                INPUT(_class="iptn", _name="prod_proveedor", requires=IS_NOT_EMPTY())
            ),
            LI('Imagen: ',
                INPUT(_class="iptn", _name="prod_imagen", requires=IS_IMAGE(extensions=('jpeg', 'png')))
            ),
            LI('Fecha de registro: ',
                INPUT(_class="iptn", _name="prod_fecha_reg", _value=str(request.now.day)+'/'+str(request.now.month)+'/'+str(request.now.year), requires=IS_NOT_EMPTY())
            ),
            LI('Fecha de Modificacion',
                INPUT(_class="iptn", _name="prod_fecha_mod", requires=IS_NOT_EMPTY())
            ),
            LI('Usuario: '
                ,INPUT(_class="iptn", _name="prod_usuario_reg", _disabled="disabled", _value=nombre, requires=IS_NOT_EMPTY())
            ),
            LI('Usuario: ',
                INPUT(_class="iptn", _name="prod_usuario_mod", requires=IS_NOT_EMPTY())
            ),
            LI('Costo: ',
                INPUT(_class="iptn", _name="prod_costo", requires=IS_NOT_EMPTY())
            ),
            LI('Margen de Utilidad: ',
                INPUT(_class="iptn", _name="prod_utilidad", requires=IS_NOT_EMPTY())
            ),
            LI('Lista de Precios: ',
                INPUT(_class="iptn", _name="prod_precio", requires=IS_NOT_EMPTY())
            )
        ),
        INPUT(_type='submit', _id='btng', _name='btng', _value='Guardar'),BR(),BR(),BR(),BR(),
    _id='form_prod'
    )

    if form.accepts(request,session):
        response.flash = 'Se ha guardado correctamente.'
    elif form.errors:
        response.flash = 'Se encontraron errores.'

    return dict(nombre=nombre,nombre_vista=nombre_vista,form=form)