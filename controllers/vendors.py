# -*- coding: utf-8 -*-

#Views
def index():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_read']
    return dict(title=title, current=current)

def new():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_new']
    states = db(db.states).select(db.states.name, db.states.id, 
                 orderby='name').as_list()
    state = DIV(*[OPTION(k['name'], _value=k['id']) for k in states])
    return dict(title=title, current=current, state=state)

def update():
    title = 'Proveedores'
    vendor_id = None
    if request.vars.id:
        vendor_id = request.vars.id
    else:
        redirect(URL(c='vendors', f='new'))
    row = db(db.vendors.id==vendor_id).select().as_list()
    row = row[0]
    if not row:
        redirect(URL(c='vendors', f='new'))

    options = [OPTION('Seleccionar', _value='')]
    states = read_states()
    if states:
        for s in states:
            if s['id']==row['state_id']:
                options += [OPTION(s['name'], _value=s['id'],
                    _selected='selected')]
            else:
                options += [OPTION(s['name'], _value=s['id'])]
    states = SELECT(_name='state', _id='state', *options)

    options = [OPTION('Seleccionar', _value='')]
    municipalities = read_municipalities(row['state_id'])
    if municipalities:
        for m in municipalities:
            if m['id']==row['municipality_id']:
                options += [OPTION(m['name'], _value=m['id'],
                    _selected='selected')]
            else:
                options += [OPTION(m['name'], _value=m['id'])]
    municipalities = SELECT(_name='municipality', _id='municipality', *options)

    options = [OPTION('Seleccionar', _value='')]
    localities = read_localities(row['municipality_id'])
    if localities:
        for l in localities:
            if l['id']==row['locality_id']:
                options += [OPTION(l['name'], _value=l['id'],
                    _selected='selected')]
            else:
                options += [OPTION(l['name'], _value=l['id'])]
    localities = SELECT(_name='locality', _id='locality', *options)
    return dict(title=title, states=states, municipalities=municipalities,
        localities=localities, **row)


def contact_information():
    title = 'Proveedores'
    return dict(title=title)

def pay_information():
    title = 'Proveedores'
    current = ['menu_catalogs', 'sidebar_vendors', 'sub_vendors_pay']
    return dict(title=title, current=current)

def sales_agents():
    title = 'Agentes de ventas'
    return dict(title=title)

def new_agent():
    title = 'Agentes de ventas'
    return dict(title=title)

def quickedit():
    return dict()

#Ajax functions
def get_municipalities():
    id = request.vars.id
    municipalities = db(db.municipalities.state_id==id).select(db.municipalities.id,
                        db.municipalities.name, orderby='name').as_list()
    municipality = DIV(*[OPTION(k['name'], _value=k['id']) for k in municipalities])
    return municipality

def get_localities():
    id = request.vars.id
    localities = db(db.localities.municipality_id==id).select(db.localities.id,
                    db.localities.name, orderby='name').as_list()
    locality = DIV(*[OPTION(k['name'], _value=k['id']) for k in localities])
    return locality

def create_vendor():
    vars = None
    name = None
    vals = dict()
    if not request.ajax or request.env.request_method != 'POST':
        raise HTTP(400)
    if request.vars and request.vars.company:
        vars = request.vars
        name = vars.company
    else:
        return ''

    vals['address'] = vars.address
    vals['state_id'] = vars.state
    vals['municipality_id'] = vars.municipality
    vals['locality_id'] = vars.locality
    vals['zip_code'] = vars.zip_code
    vals['rfc'] = vars.rfc
    vals['website'] = vars.website
    id = _create_vendor(name, **vals)
    if id:
        return str(id)
    else:
        return ''

#Functions
def _create_vendor(name, **kwargs):
    """
    Insert a vendor into the vendors database. Returns the inserted id. If
    there's an error during the insertion, returns None.

    @type name: str
    @param name: Vendors name.
    @type kwargs: keywords
    @param kwargs: Vendor attributes in db.vendors.fields.
    @rtype: int
    @return: Inserted vendors id or None.

    Example:
        >>>create_vendor('Company Name')
        1
    """
    v = db.vendors
    kwargs['name'] = name
    try:
        id = v.insert(**kwargs)
    except Exception as e:
        db.rollback()
        return None
    else:
        db.commit()
        return id


def create_vendor_contact(vendor_id, contact_type_id, description):
    """
    Insert a contact for the vendor. Returns the inserted id. If
    there's an error during the insertion, returns None.

    @type vendor_id: int
    @param vendor_id: Foreign key to db.vendors.id.
    @type type_id: int
    @param type_id: Foreign key to db.contact_types.id.
    @type description: str
    @param description: Contact information description based on the type.
    @rtype: int
    @return: Inserted vendor_contact_info id or None.

    Example:
        >>>create_vendor_contact(1, 1, '(999)999-9999')
        1
    """
    vci = db.vendor_contact_info
    try:
        id = vci.insert(vendor_id=vendor_id, contact_type_id=contact_type_id,
            description=description)
    except Exception as e:
        db.rollback()
        return None
    else:
        db.commit()
        return id


def create_agent(vendor_id, name):
    """
    Insert an agent for the vendor. Returns the inserted id. If
    there's an error during the insertion, returns None.

    @type vendor_id: int
    @param vendor_id: Foreign key to db.vendors.id.
    @type name: str
    @param name: Agent's name.
    @rtype: int
    @return: Inserted vendor_agents id or None.

    Example:
        >>>create_agent(1, 'John Doe')
        1
    """
    va = db.vendor_agents
    try:
        id = va.insert(vendor_id=vendor_id, name=name)
    except Exception as e:
        db.rollback()
        return None
    else:
        db.commit()
        return id


def create_agent_contact(agent_id, contact_type_id, description):
    """
    Insert a contact information for the agent. Returns the inserted id. If
    there's an error during the insertion, returns None.

    @type agent_id: int
    @param agent_id: Foreign key to db.vendor_agents.id.
    @type contact_type_id: int
    @param contact_type_id: Foreign key to db.contact_types.id.
    @type description: str
    @param description: Contact information description based on the type.
    @rtype: int
    @return: Inserted vendor_agent_contact_info id or None.

    Example:
        >>>create_agent_contact(1, 1, '(999)999-9999')
        1
    """
    vaci = db.vendor_agent_contact_info
    try:
        id = vaci.insert(vendor_agent_id=agent_id,
            contact_type_id=contact_type_id, description=description)
    except Exception as e:
        db.rollback()
        return None
    else:
        db.commit()
        return id

def read_states():
    states = db.states
    query = states.country_id==1
    try:
        rows = db(query).select(states.id, states.name).as_list()
    except Exception as e:
        return None
    else:
        return rows

def read_municipalities(state_id):
    m = db.municipalities
    query = m.state_id==state_id
    try:
        rows = db(query).select(m.id, m.name).as_list()
    except Exception as e:
        return None
    else:
        return rows

def read_localities(municipality_id):
    l = db.localities
    query = l.municipality_id==municipality_id
    try:
        rows = db(query).select(l.id, l.name).as_list()
    except Exception as e:
        return None
    else:
        return rows

def update_vendor(vendor_id, **kwargs):
    """
    Updates vendor's information with the given identifies. Returns True on
    success.

    @param vendor_id: vendor's identifier.
    @type vendor_id: int
    @param kwargs: Keywords in db.vendors.fields.
    @type kwargs: keywords
    @return: True on success, False otherwise.
    @rtype: bool

    Example:
        >>>update_vendor(1, name='Apple')
        True
    """
    try:
        db.vendors[vendor_id] = kwargs
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True


def update_vendor_contact_info(vendor_contact_info_id, **kwargs):
    """
    Updates vendor's information with the given identifies. Returns True on
    success.

    @param vendor_contact_info_id: contact's identifier
    @type vendor_contact_info_id: int
    @param kwargs: Keywords in db.vendor_contact_info.fields.
    @type kwargs: keywords
    @return: True on success, False otherwise.
    @rtype: bool

    Example:
        >>>kwargs = dict(contact_type_id=1, description='steve@apple.com')
        >>>update_vendor_contact_info(1, **kwargs)
        True
    """
    try:
        db.vendor_contact_info[vendor_contact_info_id] = kwargs
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True


def update_vendor_agent(vendor_agent_id, **kwargs):
    """
    Updates agent's information with the given identifier. Returns True on
    success.

    @param vendor_agent_id: vendor's agent identifier in db.vendor_agents.id.
    @type vendor_agent_id: int
    @param kwargs: Keywords in db.vendor_agents.fields.
    @type kwargs: keywords
    @return: True on success, False otherwise.
    @rtype: bool

    Example:
        >>>update_vendor_agent(1, name='John Doe')
    """
    try:
        db.vendor_agents[vendor_agent_id] = kwargs
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True


def update_vendor_agent_contact_info(vendor_agent_contact_info_id, **kwargs):
    """
    Updates the contact information of a vendor's agent with the given
    identifier. Returns True on success.

    @param vendor_agent_contact_info_id: The identifier of an agent's contact
    information in db.vendor_agent_contact_info.id.
    @type vendor_agent_contact_info_id: int
    @param kwargs: Keywords in db.vendor_agent_contact_info.fields
    @type kwargs: keywords
    @return: True on success, False otherwise.
    @rtype: bool

    Example:
        >>>update_vendor_agent_contact_info(1)
        True
    """
    try:
        db.vendor_agent_contact_info[vendor_agent_contact_info_id] = kwargs
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True


def delete_vendor(vendor_id):
    """
    Deletes a vendor with the given id. Return True on success.

    B{Note:}
    B{Using this function may end in the deletion of ALL records attached
    with the given vendor id.}

    @param vendor_id: record's id of the vendor to delete.
    @type vendor_id:int
    @return: True on success, False otherwise.
    @rtype: bool

    Example:
        >>>delete_vendor(1)
        True
    """
    try:
        del db.vendors[vendor_id]
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True


def delete_vendor_contact_info(vendor_contact_info_id):
    """
    Deletes the vendor contact info with de given id. Returns True on success.

    @param vendor_contact_info_id: The identifier of the vendor contact info.
    @type vendor_contact_info_id: int
    @return: True on success, False otherwise.
    @rtype: bool

    Example:
        >>>delete_vendor_contact_info(1)
        True
    """
    try:
        del db.vendor_contact_info[vendor_contact_info_id]
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True


def delete_vendor_agent(vendor_agent_id):
    """
    Deletes an agent with the given id. Return True on success.

    B{Note:}
    B{Using this function may end in the deletion of ALL records attached
    with the given agent id.}

    @param vendor_agent_id: The identifier of the agent.
    @type vendor_agent_id: int
    @return: True on success, False otherwise.
    @rtype: bool

    Example:
        >>>delete_vendor_agent(1)
        True
    """
    try:
        del db.vendor_agents[vendor_agent_id]
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True


def delete_vendor_agent_contact_info(vendor_agent_contact_info_id):
    """
    Deletes the agent's contact information with the given id. Returns True
    on success.

    @param vendor_agent_contact_info_id:
    @type vendor_agent_contact_info_id:
    @return: True on success. False otherwise.
    @rtype: bool

    Example:
        >>>delete_vendor_agent_contact_info(1)
        True
    """
    try:
        del db.vendor_agent_contact_info[vendor_agent_contact_info_id]
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True
