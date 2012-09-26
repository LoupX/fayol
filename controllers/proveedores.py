#@auth.requires_login()
nombre = 'Emir Salazar'
nombre_vista = ''

def index():
    dum = 'Aqui va las apps'
    dum1 = 'notificaciones'
    nombre_vista = 'Dashboard'
    return dict(dum=dum, dum1=dum1, nombre=nombre, nombre_vista=nombre_vista)

def proveedor():
    nombre_vista = 'Proveedores'
    return dict(nombre=nombre, nombre_vista=nombre_vista)

def nuevoproveedor():
    if request.vars:
        #vars for ventors
        company = request.vars['empresa']
        address = request.vars['direccion']
        state = request.vars['estado']
        code = request.vars['cp']
        municipality = request.vars['municipio']
        rfc = request.vars['rfc']
        city = request.vars['ciudad']
        site = request.vars['sitio']

        #vars for paid method
        bank = request.vars['banco']
        account = request.vars['cuenta']
        branch = request.vars['sucursal']
        clabe = request.vars['clabe']

        shit = dict(address=address, state=state, zip_code=code,
                    municipality=municipality, rfc=rfc, city=city, website=site,
                    bank=bank, bank_account_number=account, branch=branch,
                    clabe=clabe)

        inserto = create_vendor(company, **shit)
        sin = str(inserto)

        #contact's method
        my_list = []
        my_lisd = []
        for n in request.vars:
            if n.startswith('tipo-contacto-'):
                #my_list.append(request.vars[n])
                my_list.append(n)
                #create_vendor_contact(7, request, description)
            if n.startswith('campo-contacto-'):
                #my_list.append(request.vars[n])
                my_lisd.append(n)

        my_list.sort()
        my_lisd.sort()
        l = len(my_list)


        if sin != 'None':
            for c in range(0, l):
                inserto_con = create_vendor_contact(inserto,
                                                    1,
                                                    request.vars[my_lisd[c]])
                response.write(str(inserto) + request.vars[my_list[c]] +
                               request.vars[my_lisd[c]])

        sinc = str(inserto_con)
        response.write("Respuesta: {}".format(inserto_con))

        if sin != 'None' and sinc != 'None':
            response.flash = 'Se ha guardado.'
        else:
            response.flash = 'Ocurrio un error.'

    nombre_vista = 'Proveedores'
    estados = db(db.states).select(db.states.name,
        db.states.id, orderby='name').as_list()
    estado = DIV(*[OPTION(k['name'], _value=k['id']) for k in estados])
    bancos = db(db.banks).select(db.banks.short_name,
        db.banks.id, orderby='short_name').as_list()
    banco = DIV(*[OPTION(b['short_name'], _value=b['id']) for b in bancos])
    return dict(nombre=nombre, nombre_vista=nombre_vista, estado=estado,
        banco=banco)

def sel_municipio():
    id = request.vars.id
    municipios = db(db.municipalities.state_id==id).select(db.municipalities.id,
        db.municipalities.name, orderby='name').as_list()
    municipio = DIV(*[OPTION(k['name'], _value=k['id']) for k in municipios])

    return municipio;

def sel_ciudad():
    id = request.vars.id
    ciudades = db(db.localities.municipality_id==id).select(db.localities.id,
        db.localities.name, orderby='name').as_list()
    ciudad = DIV(*[OPTION(k['name'], _value=k['id']) for k in ciudades])
    return ciudad;

def guardar():
    name = request.vars.empresa
    create_vendor(request.vars);
    return dict();

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
                DIV(
                    INPUT( _name="prod_estado", _type="radio", _value='1', _id='a', requires=IS_NOT_EMPTY()),LABEL('Activar', _for='a'),
                    INPUT( _name="prod_estado", _type="radio", _value='0', _id='d', requires=IS_NOT_EMPTY()),LABEL('Desactivar', _for='d')
                )
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

def autocomplete():
    return dict(nombre=nombre,nombre_vista=nombre_vista)

def month_selector():
    if not request.vars.month: return ''
    #months = ['January', 'February', 'March', 'April', 'May',
    #          'June', 'July', 'August', 'September' ,'October',
    #          'November', 'December']
    months = db(db.states).select(db.states.name, db.states.id).as_list()
    month_start = request.vars.month.capitalize()
    selected = [m for m in months if m['name'].startswith(month_start)]
    return DIV(*[OPTION(k['name'], _value=k['id']) for k in selected])

