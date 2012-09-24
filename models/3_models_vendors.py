# -*- coding: utf-8 -*-

db.define_table('vendors',
    Field('name', 'string', required=True, notnull=True, label=T('Nombre'),
        unique=True),
    Field('address', 'string', label=T('Dirección')),
    Field('city', 'string', label=T('Ciudad')),
    Field('municipality', 'string', label=T('Municipio')),
    Field('state', 'string', label=T('Estado')),
    Field('zip_code', 'integer', length=5, label=T('Código postal')),
    Field('rfc', 'string', length=13, label='RFC'),
    Field('website', 'string', label=T('Sitio web')),
    Field('bank', 'string', label=T('Banco')),
    Field('bank_account_number', 'integer', label=T('Número de cuenta')),
    Field('branch', 'string', label=T('Sucursal')),
    Field('clabe', 'integer', length=18, label='CLABE'),
    Field('status', 'boolean', default=True, label=T('Estado')),
    Field('date_added', 'datetime', default=request.now, writable=False,
      readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False,
      readable=False),
    Field('added_by', 'references auth_user',
      default=auth.user.id if auth.user else 0),
    Field('modified_by', 'references auth_user',
      update=auth.user.id if auth.user else 0),
    format='%(name)s')

db.define_table('vendor_contact_info',
    Field('vendor_id', 'references vendors', notnull=True),
    Field('contact_type_id', 'references contact_types', notnull=True,
        label=T('Tipo')),
    Field('description', 'string', notnull=True, label=T('Descripción')))

db.define_table('vendor_agents',
    Field('vendor_id', 'references vendors', notnull=True),
    Field('name', 'string', required=True, notnull=True, label=T('Nombre')),
    format='%(name)s')

db.define_table('vendor_agent_contact_info',
    Field('vendor_agent_id', 'references vendor_agents', notnull=True),
    Field('contact_type_id', 'references contact_types', notnull=True,
        label=T('Tipo')),
    Field('description', 'string', notnull=True, label=T('descripción')))

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
    vendor = dict()
    v = db.vendors

    if not name:
        return None
    if type(kwargs) is dict:
        vendor = kwargs
    vendor['name'] = name

    for key in vendor:
        if not key in v.fields:
            del vendor[key]

    try:
        id = v.bulk_insert([vendor])[0]
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
    if not vendor_id or not contact_type_id or not description:
        return None

    try:
        id = vci.insert(vendor_id=vendor_id, contact_type_id=contact_type_id,
            description=description)
    except Exception as e:
        db.rollback()
        return None

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
    id = None

    if not vendor_id or not name:
        return None

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
    id = None

    if not agent_id or not contact_type_id or not description:
        return None

    try:
        id = vaci.insert(vendor_agent_id = agent_id,
            contact_type_id=contact_type_id, description=description)
    except Exception as e:
        db.rollback()
        return None
    else:
        db.commit()
        return id

def read_vendors(min, max):
    rows = db().select(db.vendors.ALL, limitby=(0, 2))
    return rows.as_list()

def read_vendor_contacts(vendor_id, min, max):
    rows = db(db.vendor)

def update_vendor(table, id, **kwargs):
    """
    Updates the given vendor information according to the table. Returns True
    on succed, False if not.
    @type table: int
    @param table: It is used to select the table to update. It can be any of
    the following values:
        1. vendors

        2. vendor_contact_info

        3. vendor_agents

        4. vendor_agent_contact_info
    @type id: int
    @param id: The id of the record to update.
    @type kwargs: keywords
    @param kwargs: Must be in db.table.fields. I{table} stands for the
    selected table identidicator.
    @rtype: bool
    @return: True or False.

    Example:
        >>>update_vendor(1, 1, name='Another Company Name')
        True
    """
    if table == 1:
        t = db.vendors
    elif table == 2:
        t = db.vendor_contact_info
    elif table == 3:
        t = db.vendor_agents
    elif table == 4:
        t = db.vendor_agent_contact_info
    else:
        return False
    if not kwargs:
        return False

    try:
        for key in kwargs:
            if not key in t.fields:
                del kwargs[key]
        t[id] = kwargs
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True

def delete_vendor(table, id):
    """
    Deletes the given vendor information according to the table. Returns True
    on succed, False if not.

    @type table: int
    @param table: It is used to select the table to update. It can be any of
    the following values:
        2. vendor_contact_info

        3. vendor_agents

        4. vendor_agent_contact_info
    @type id: int
    @param id: The id of the record to delete.
    @rtype: bool
    @return: True or False

    Example:
        >>>delete_vendor(2, 1)
        True
    """
    if table == 2:
        t = db.vendor_contact_info
    elif table == 3:
        t = db.vendor_agents
    elif table == 4:
        t = db.vendor_agent_contact_info
    else:
        return False

    try:
        del t[id]
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True
