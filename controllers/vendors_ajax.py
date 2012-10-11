# -*- coding: utf-8 -*-

#Ajax functions
def get_vendors():
    v = db.vendors
    rows = db(v.status==True).select(v.name, v.id)
    options = str()
    for row in rows:
        options += str(OPTION(row.name, _value=row.id))
        options += '\n'
    return options

def get_vendor_info():
    info = dict()
    info['name'] = None
    info['address'] = None
    info['state'] = None
    info['municipality'] = None
    info['locality'] = None
    info['zip_code'] = None
    info['rfc'] = None
    info['website'] = None
    info['bank'] = None
    info['branch_number'] = None
    info['account_number'] = None
    info['clabe'] = None
    info['status'] = None

    vendor_id = None
    if request.vars.id:
        try:
            vendor_id = int(request.vars.id)
        except:
            return info
    else:
        return info
    row = db(db.vendors.id==vendor_id).select().first()
    if not row:
        return info

    info['name'] = row.name
    info['address'] = row.address
    info['state'] = row.state_id
    info['municipality'] = row.municipality_id
    info['locality'] = row.locality_id
    info['zip_code'] = row.zip_code
    info['rfc'] = row.rfc
    info['website'] = row.website
    info['bank'] = row.bank_id
    info['branch_number'] = row.branch
    info['account_number'] = row.bank_account_number
    info['clabe'] = row.clabe
    info['status'] = row.status
    return info


def create_vendor():
    vars = None
    name = None
    vals = dict()

    if request.vars and request.vars.company:
        vars = request.vars
        name = vars.company
    else:
        return ''
    try:
        vals['address'] = vars.address
        vals['state_id'] = vars.state
        vals['municipality_id'] = vars.municipality
        vals['locality_id'] = vars.locality
        vals['zip_code'] = vars.zip_code
        vals['rfc'] = vars.rfc
        vals['website'] = vars.website
    except Exception as e:
        return ''

    id = _create_vendor(name, **vals)
    if id:
        return str(id)
    else:
        return ''

def update_vendor():
    vars = None
    vendor_id = None
    name = None
    vals = dict()
    if not request.ajax or request.env.request_method != 'POST':
        raise HTTP(400)

    if request.vars and request.vars.company and session.vendor_id:
        vars = request.vars
        vals['name'] = vars.company
        vendor_id = session.vendor_id
    else:
        return ''
    try:
        vals['address'] = vars.address
        vals['state_id'] = vars.state
        vals['municipality_id'] = vars.municipality
        vals['locality_id'] = vars.locality
        vals['zip_code'] = vars.zip_code
        vals['rfc'] = vars.rfc
        vals['website'] = vars.website
    except Exception as e:
        return ''

    r = _update_vendor(vendor_id, **vals)
    if r:
        return 'true'
    else:
        return ''

def create_pay_information():
    data = dict()
    id = None
    if not request.vars.id:
        return ''
    else:
        id = request.vars.id
    try:
        data['branch'] = request.vars.branch
        data['bank_account_number'] = request.vars.bank_account_number
        data['clabe'] = request.vars.clabe
    except Exception as e:
        pass

    v = db.vendors
    query = v.id==id
    try:
        db(query).update(**data)
    except Exception as e:
        db.rollback()
        return ''
    else:
        db.commit()
        return True

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

def _update_vendor(vendor_id, **kwargs):
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
        r = db(db.vendors.id==vendor_id).update(**kwargs)
        if r==0:
            raise Exception('Record does not exist')
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True

def _update_vendor_contact_info(vendor_contact_info_id, **kwargs):
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
        r = db(db.vendor_contact_info.id==vendor_contact_info_id).update(
            **kwargs)
        if r == 0:
            raise Exception('Record does not exist')
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True


def _update_vendor_agent(vendor_agent_id, **kwargs):
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
        r = db(db.vendor_agents.id==vendor_agent_id).update(**kwargs)
        if r == 0:
            raise Exception('Record does not exist')
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True


def _update_vendor_agent_contact_info(vendor_agent_contact_info_id, **kwargs):
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
    vaci = db.vendor_agent_contact_info
    try:
        r = db(vaci.id==vendor_agent_contact_info_id).update(**kwargs)
        if r == 0:
            raise Exception('Record does not exist')
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
