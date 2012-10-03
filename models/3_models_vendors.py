# -*- coding: utf-8 -*-
db.define_table('vendors',
    Field('name', 'string', notnull=True, unique=True),
    Field('address', 'string'),
    Field('city', 'string'),
    Field('municipality', 'string'),
    Field('state', 'string'),
    Field('zip_code', 'integer', length=5),
    Field('rfc', 'string', length=13),
    Field('website', 'string'),
    Field('bank', 'string'),
    Field('bank_account_number', 'string'),
    Field('branch', 'string'),
    Field('clabe', 'string', length=18),
    Field('status', 'boolean', default=True),
    Field('date_added', 'datetime', default=request.now),
    Field('date_modified', 'datetime', update=request.now),
    Field('added_by', 'reference auth_user',
      default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
      update=auth.user.id if auth.user else 0), migrate=MIGRATE)

db.define_table('vendor_contact_info',
    Field('vendor_id', 'reference vendors', notnull=True),
    Field('contact_type_id', 'reference contact_types', notnull=True,
        label=T('Tipo')),
    Field('description', 'string', notnull=True), migrate=MIGRATE)

db.define_table('vendor_agents',
    Field('vendor_id', 'reference vendors', notnull=True),
    Field('name', 'string', required=True, notnull=True),
    migrate=MIGRATE)

db.define_table('vendor_agent_contact_info',
    Field('vendor_agent_id', 'reference vendor_agents', notnull=True),
    Field('contact_type_id', 'reference contact_types', notnull=True),
    Field('description', 'string', notnull=True), migrate=MIGRATE)

db.vendors.date_added.represent = (
    lambda date_added, row: date_added.strftime('%d - %m - %Y'))
db.vendors.date_modified.represent = ( 
    lambda date_modified, row: date_added.strftime('%d - %m - %Y'))

def create_vendor(name, **kwargs):
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
        id = vaci.insert(vendor_agent_id = agent_id,
            contact_type_id=contact_type_id, description=description)
    except Exception as e:
        db.rollback()
        return None
    else:
        db.commit()
        return id

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

