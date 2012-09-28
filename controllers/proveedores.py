#@auth.requires_login()
nombre = 'Emir Salazar'
nombre_vista = ''

def index():
    nombre_vista = 'Dashboard'
    form = FORM(INPUT(_name='u', requires=IS_NOT_EMPTY()),INPUT(_name='p'),
                INPUT(_type='submit'))
    if form.accepts(request,session):
        #option 1
        response.flash = 'good'
    elif form.errors:
        #option 2
        response.flash = 'wrong'
    return dict(nombre=nombre, nombre_vista=nombre_vista, form=form)

def proveedor():
    nombre_vista = 'Proveedores'
    return dict(nombre=nombre, nombre_vista=nombre_vista)

def nuevoproveedor():
    if request.post_vars['btng'] == 'Guardar':

        #bolempresa = True if request.post_vars['empresa'] else False
        #if not bolempresa:
        #    response.flash = 'Favor de ingresar el nombre del Proveedor.'
        #check if request.post_vars['empresa'] then search in db for
        # duplicates
        bolempresa = False
        if request.post_vars['empresa']:
            estaa = db(db.vendors.name==request.post_vars['empresa']).select(db.vendors.name)
            if estaa:
                response.flash = 'Ya existe un Proveedor con ese nombre.'
            else:
                bolempresa = True
        else:
            bolempresa = False

        bolcode = True
        #response.write(len(request.vars['cp']))
        if request.post_vars['cp']:
            try:
                code = int(request.post_vars['cp'])
                #response.write(request.vars['cp'])
                if len(request.post_vars['cp']) == 5:
                    bolcode = True
                else:
                    bolcode = False
                    response.flash = 'Código postal inválido.'
            except:
                bolcode = False
                response.flash = 'Código postal inválido.'


        if bolempresa == True and bolcode == True :
            #save
            #vars for vendors
            company = request.post_vars['empresa']
            address = request.post_vars['direccion']
            state = request.post_vars['estado']
            code = request.post_vars['cp']
            municipality = request.post_vars['municipio']
            rfc = request.post_vars['rfc']
            city = request.post_vars['ciudad']
            site = request.post_vars['sitio']

            #vars for paid method
            bank = request.post_vars['banco']
            account = request.post_vars['cuenta']
            branch = request.post_vars['sucursal']
            clabe = request.post_vars['clabe']

            shit = dict(address=address, state=state, zip_code=code,
                municipality=municipality, rfc=rfc, city=city, website=site,
                bank=bank, bank_account_number=account, branch=branch,
                clabe=clabe)

            #contact's method
            my_list = []
            my_lisd = []
            for n in request.post_vars:
                if n.startswith('tipo-contacto-'):
                    try:
                        nint = int(request.post_vars[n])
                        if type(nint) is int:
                            my_list.append(n)
                            #response.write(type(int(request.post_vars[n])))
                    except:
                        response.write('oops!')
                if n.startswith('campo-contacto-'):
                    my_lisd.append(n)
            my_list.sort()
            my_lisd.sort()
            l = len(my_list)
            nos = []

            #insert vendor's name and shit
            inserto = create_vendor(company, **shit)
            sin = str(inserto)
            #sin = str(inserto) if inserto is int else 'None'
            insertocon = 0
            if sin != 'None':
                for c in range(0, l):
                    nos.append(request.post_vars[my_list[c]]+'-'+request.post_vars[my_lisd[c]])
                    insertocon = create_vendor_contact(inserto, int(request.post_vars[my_list[c]]), request.post_vars[my_lisd[c]])
            else:
                response.flash = 'No se guardo los datos del Proveedor.'
            sinc = str(insertocon)
            #sinc = str(insertocon) if insertocon is int else 'None'

            if sin != 'None' and sinc != 'None':
                if sinc != '0':
                    response.flash = 'Se han guardado los datos.'
                else:
                    sup = True #delete_vendor(insertocon)
                    if sup:
                        response.flash = 'Ocurrio un error con los datos de '\
                                         'contacto.'
                    else:
                        response.flash = 'Fatal error. :S'
            else:
                response.flash = 'Ocurrio un error al guardar los datos.'

                #response.write(company)
                #response.write('<br>', escape=False)
                #response.write(shit)
                #response.write('<br>', escape=False)
                #response.write(my_list)
                #response.write('<br>', escape=False)
                #response.write(nos)
                #response.write('<br>', escape=False)
                #response.write('proveedor: '+sin)
                #response.write('<br>', escape=False)
                #response.write('contacto: '+sinc)
                #else:
                #response.flash = 'Favor de ingresar el nombre del Proveedor.'

    nombre_vista = 'Agregar Proveedor'
    estados = db(db.states).select(db.states.name, db.states.id,
        orderby='name').as_list()
    estado = DIV(*[OPTION(k['name'], _value=k['id']) for k in estados])
    bancos = db(db.banks).select(db.banks.short_name, db.banks.id,
        orderby='short_name').as_list()
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


def nuevoagente():
    nombre_vista = 'Proveedores'
    nombre = 'Jose'
    return dict(nombre=nombre, nombre_vista=nombre_vista)
