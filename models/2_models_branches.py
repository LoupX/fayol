# -*- coding: utf-8 -*-
db.define_table('company_addresses',
    Field('address', 'string', notnull=True),
    Field('suburb', 'string', comment='colonia', notnull=True),
    Field('country_id', 'reference countries', default=1),
    Field('state_id', 'reference states', notnull=True),
    Field('municipality_id', 'reference municipalities'),
    Field('locality_id', 'reference localities', notnull=True),
    Field('zip_code', 'integer', length=5),
    Field('status', 'boolean', default=True, label=T('Estado')),
    Field('date_added', 'datetime', default=request.now, writable=False,
      readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False,
      readable=False),
    Field('added_by', 'reference auth_user',
      default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
      update=auth.user.id if auth.user else 0), migrate=MIGRATE)

db.define_table('company_tax_info',
    Field('business_name', 'string', comment='razón social'),
    Field('rfc', 'string', length='13', unique=True),
    Field('tax', 'string', comment='régimen fiscal'),
    Field('status', 'boolean', default=True, label=T('Estado')),
    Field('date_added', 'datetime', default=request.now, writable=False,
      readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False,
      readable=False),
    Field('added_by', 'reference auth_user',
      default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
      update=auth.user.id if auth.user else 0), migrate=MIGRATE)

db.define_table('branches',
    Field('name', 'string', notnull=True, unique=True),
    Field('company_address_id', 'reference company_addresses'),
    Field('company_tax_info_id', 'reference company_tax_info'),
    Field('status', 'boolean', default=True, label=T('Estado')),
    Field('date_added', 'datetime', default=request.now, writable=False,
      readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False,
      readable=False),
    Field('added_by', 'reference auth_user',
      default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
      update=auth.user.id if auth.user else 0), migrate=MIGRATE)

db.define_table('warehouses',
    Field('name', 'string', notnull=True, unique=True),
    Field('company_address_id', 'reference company_addresses'),
    Field('status', 'boolean', default=True, label=T('Estado')),
    Field('date_added', 'datetime', default=request.now, writable=False,
      readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False,
      readable=False),
    Field('added_by', 'reference auth_user',
      default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
      update=auth.user.id if auth.user else 0), migrate=MIGRATE)

def create_company_address(address, suburb, state_id,
                           locality_id,  **kwargs):
    """
    Inserts a new company address. Returns the inserted id.

    @param address: Company address.
    @type address: str
    @param suburb: Company 'colonia'.
    @type suburb: str
    @param state_id: Foreign key to db.states.id.
    @type state_id: int
    @param locality_id: Foreign key to db.localities.id
    @type locality_id: int
    @param kwargs: Keywords in db.company_addresses.fields.
    @type kwargs: keywords
    @return: The inserted id on succed, None otherwise.
    @rtype: int

    Example:
        >>>create_company_address('street 1', 'downtown', 1, 1)
        1
    """
    company_addresses_id = None
    kwargs['address'] = address
    kwargs['suburb'] = suburb
    kwargs['state_id'] = state_id
    kwargs['locality_id'] = locality_id
    try:
        id = db.company_addresses.insert(**kwargs)
    except Exception as e:
        db.rollback()
        return None
    else:
        db.commit()
        return company_addresses_id


def create_company_tax_info(**kwargs):
    """
    Inserts a new company tax information. Returns the inserted id.

    @param kwargs: keywords in db.company_tax_info.fields.
    @type kwargs: keywords
    @return: The inserted id on succed, None otherwise.
    @rtype: int

    Exaxple:
        >>>create_company_tax_info('Apple Inc.')
        1
    """
    company_tax_info_id = None
    try:
        company_tax_info_id = db.company_tax_info.insert(**kwargs)
    except Exception as e:
        db.rollback()
        return None
    else:
        db.commit()
        return company_tax_info_id

def create_branch(name, company_address_id=None, company_tax_info_id=None):
    """
    Inserts a new branch. Returns the inserted id.

    @param name: The name of the branch.
    @type name: str
    @param company_address_id: Foreign key to db.company_addresses.id.
    @type company_address_id: int
    @param company_tax_info_id: Foreign to db.company_tax_info.id.
    @type company_tax_info_id: int
    @return: The inserted id on succed, None otherwise.
    @rtype: int

    Example:
        >>>create_branch('Apple NY.')
        1
    """
    branch_id = None
    insert = dict(name=name, address_id=address_id,
        company_tax_info_id=company_tax_info_id)
    try:
        branch_id = db.branches.insert(**insert)
    except Exception as e:
        db.rollback()
        return None
    else:
        db.commit()
        return branch_id

def create_warehouse(name, company_address_id=None):
    """

    @param name: The name of the new warehouse.
    @type name: str
    @param company_address_id: Foreign key to db.company_addresses.id.
    @type company_address_id: int
    @return: The inserted id on succed, None otherwise.
    @rtype: int

    Example:
        create_warehouse('East warehouse')
        1
    """
    warehouse_id = None
    insert = dict(name=name, company_address_id=company_address_id)
    try:
        warehouse_id = db.warehouses.insert(**insert)
    except Exception as e:
        db.rollback()
        return None
    else:
        db.commit()
        return warehouse_id

def update_company_address(company_address_id, **kwargs):
    """
    Updates a company's address information with the given identifier.
    Returns True on success.

    @param company_address_id: identifier for company_addresses.
    @type company_address_id: int
    @param kwargs: Keywords in db.company_addresses.fields
    @type kwargs: keywords
    @return: True on succed, False otherwise
    @rtype: bool

    Example:
        >>>update_company_address(1, address='5th street')
        True
    """
    try:
        db.company_addresses[company_address_id] = kwargs
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True

def update_company_tax_info(company_tax_info_id, **kwargs):
    """
    Updates a comany's tax info with the given identifier. Returns True on
    success.

    @param company_tax_info_id: An identifier in db.company_tax_info.id.
    @type company_tax_info_id: int
    @param kwargs: Keywords in db.company_tax_info.fields.
    @type kwargs: keywords
    @return: True on success, False otherwise.
    @rtype: bool

    Example:
        >>>update_company_tax_info(1, rfc='XXXX000000XXX')
        True
    """
    id = company_tax_info_id
    try:
        db.company_tax_info[id] = kwargs
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return None

def update_branch(branch_id, **kwargs):
    """
    Updates branch's information with the given identifier. Returns True on
    success.
    @param branch_id: An identifier in db.branches.id.
    @type branch_id: int
    @param kwargs: Keywords in db.branches.fields.
    @type kwargs: keywords
    @return: True on success, False otherwise.
    @rtype: bool

    Example:
        >>>update_branch(1, name='Apple iShop')
        True
    """
    try:
        db.branches[branch_id] = kwargs
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True

def update_warehouse(warehouse_id, **kwargs):
    """
    Updates warehouse's information with the given identifier. Returns True
    on success.

    @param warehouse_id: An identifier in db.warehouses.id.
    @type warehouse_id: int
    @param kwargs: Keywords in db.warehouses.fields.
    @type kwargs: keywords
    @return: True on success, False otherwise.
    @rtype: bool

    Example:
        >>>update_warehouse(1, name='Blender's stock')
        True
    """
    try:
        db.warehouses[warehouse_id] = kwargs
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True
