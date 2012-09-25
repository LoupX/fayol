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
    nombre_vista = 'Proveedores'
    return dict(nombre=nombre, nombre_vista=nombre_vista)

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
    months = ['January', 'February', 'March', 'April', 'May',
              'June', 'July', 'August', 'September' ,'October',
              'November', 'December']
    month_start = request.vars.month.capitalize()
    selected = [m for m in months if m.startswith(month_start)]
    return UL(*[LI(k) for k in selected])

