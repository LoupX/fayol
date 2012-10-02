# -*- coding: utf-8 -*-

db.define_table('products',
    Field('brand_id', 'reference brands', required=True, notnull=True),
    Field('unit_id', 'reference units', required=True, notnull=True),
    Field('code', 'string', required=True, notnull=True, unique=True),
    Field('alternative_code', 'string'),
    Field('location', 'string'),
    Field('part_number', 'string'),
    Field('serial_number', 'string'),
    Field('model', 'string'),
    Field('image', 'upload', uploadfield=True),
    Field('standard_cost', 'decimal(10,2)'),
    Field('markup', 'decimal(3,2)'),
    Field('status', 'boolean'),
    Field('date_added', 'datetime', default=request.now, writable=False,
	  readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False,
	  readable=False),
    Field('added_by', 'reference auth_user',
	  default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
	  update=auth.user.id if auth.user else 0))

db.define_table('product_descriptions',
    Field('product_id', 'reference products', required=True, notnull=True),
    Field('name', 'string', required=True, notnull=True),
    Field('alternative_name', 'string'),
    Field('description', 'text'),
    Field('meta_description', 'string'),
    Field('meta_keywords', 'string'))

db.define_table('product_to_vendor',
    Field('product_id', 'reference products'),
    Field('vendor_id', 'reference vendors'))

db.define_table('product_to_category',
    Field('product_id', 'reference products'),
    Field('category_id', 'reference categories'))

db.define_table('product_price_lists',
    Field('product_id', 'reference products', required=True, notnull=True),
    Field('name', 'string', required=True, notnull=True),
    Field('price', 'decimal(10,2)', default=0.00),
    Field('is_default', 'boolean', default=False),
    Field('status', 'boolean', default=True),
    Field('date_added', 'datetime', default=request.now, writable=False,
	  readable=False),
    Field('date_modified', 'datetime', update=request.now, writable=False,
	  readable=False),
    Field('added_by', 'reference auth_user',
	  default=auth.user.id if auth.user else 0),
    Field('modified_by', 'reference auth_user',
	  update=auth.user.id if auth.user else 0))

db.products.date_added.represent = lambda date_added, row: date_added.strftime('%d - %m - %Y')
db.products.date_modified.represent = lambda date_modified, row: date_added.strftime('%d - %m - %Y')
db.product_price_lists.date_added.represent = lambda date_added, row: date_added.strftime('%d - %m - %Y')
db.product_price_lists.date_modified.represent = lambda date_modified, row: date_added.strftime('%d - %m - %Y')

def create_product(name, code, brand_id, unit_id, categories, **kwargs):
    """
    Insert all product values but prices an returns a dictionary with the
    inserted id's.

    @param name: Product name.
    @type name: str
    @param code: Custom product code.
    @type code: str
    @param brand_id: Foreign key to db.brands.id.
    @type brand_id: int
    @param unit_id: Foreign key to db.units.id.
    @type unit_id: int
    @param categories: List of foreign keys to db.categories.id.
    @type categories: list
    @param kwargs: Product attributes in the following tables:
        1. db.products.fields.
        2. db.product_descriptions.fields.
        3. db.product_to_vendor.fields.
        4. db.product_to_category.fields.
    @type kwargs: keywords
    @return: A dictionary of the inserted fields.
    @rtype: dict
    """
    product_id = None
    product_description_id = None
    product_to_category_ids = []
    product_to_vendor_ids = []

    insert = dict(code=code, brand_id=brand_id, unit_id=unit_id)
    for key in kwargs:
        if key in db.products.fields:
            insert[key] = kwargs[key]
            del kwargs[key]
    try:
        product_id = db.products.insert(**insert)
    except Exception as e:
        db.rollback()
        return None
    else:
        db.commit()

    insert = dict(product_id=product_id, name=name)
    for key in kwargs:
        if key in db.product_descriptions.fields:
            insert[key] = kwargs[key]
            del kwargs[key]
    try:
        product_description_id = db.product_descriptions.insert(**insert)
    except Exception as e:
        db.rollback()
    else:
        db.commit()

    if type(categories) is list:
        for category_id in categories:
            try:
                product_to_category_ids.append(
                    db.product_to_category.insert(product_id=product_id,
                        category_id=category_id))
            except Exception as e:
                db.rollback()
            else:
                db.commit()

    vendors = kwargs['vendors']
    if type(vendors) is list:
        for vendor_id in vendors:
            try:
                product_to_vendor_ids.append(
                    db.product_to_vendor.insert(
                        product_id=product_id,
                        vendor_id=vendor_id))
            except Exception as e:
                db.rollback()
            else:
                db.commit()

    r = dict(product_id=product_id,
             product_description_id=product_description_id,
             product_to_category_ids=product_to_category_ids,
             product_to_vendor_ids=product_to_vendor_ids)
    return r

def create_price(product_id, name, price, is_default=False):
    """
    Inserts an record in the price list. Returns the inserted id.

    If is_default is set to True, any other price set as default in the price
    list is set to False.

    @param product_id: Foreign key to db.products.id
    @type product_id: int
    @param name: The name of the record in the price list.
    @type name: str
    @param price: The value for the record. It can only have two decimals.
    @type price: float
    @param is_default: An optional keyword with the is_default keyword.
    @type is_default: bool
    @return: The inserted record id.
    @rtype: int
    """
    product_price_list_id = None
    ppl = db.product_price_lists
    if is_default:
        query = ppl.product_id==product_id
        query &= ppl.is_default==True
        try:
            db(query).update(is_default=False)
        except Exception as e:
            db.rollback()
            return None
        else:
            db.commit()
        try:
            product_price_list_id = db.product_price_lists.insert(
                product_id=product_id,name=name, price=price,
                is_default=True)
        except Exception as e:
            db.rollback()
            return None
        else:
            db.commit()
            return product_price_list_id
    else:
        try:
            product_price_list_id = db.product_price_lists.insert(
                product_id=product_id, name=name, price=price,
                is_default=True)
        except Exception as e:
            db.rollback()
            return None
        else:
            db.commit()
            return product_price_list_id


def update_product(product_id, **kwargs):
    """
    Updates product's main data. Returns True on suceed or False if not.

    @param product_id: Foreign key to db.products.id.
    @type product_id: int
    @param kwargs: Product attributes in db.products.fields.
    @type kwargs: keywords
    @return: True on succed, False otherwise.
    @rtype: bool
    """
    try:
        db.products[product_id] = kwargs
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True

def update_product_description(product_description_id, **kwargs):
    """
    Updates the product description. Return True on succed or False otherwise.

    @param product_description_id: Foreign key to db.product_descriptions.id.
    @type product_description_id: int
    @param kwargs: Description attributes in db.product_descriptions.fields.
    @type kwargs: keywords
    @return: True on succed, False otherwise.
    @rtype: bool
    """
    try:
        db.product_descriptions[product_description_id] = kwargs
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True


def update_product_category(product_to_category_id, **kwargs):
    """
    Updates the product to category relationship. Return True on succed or
    False otherwise.

    @param product_to_category_id: Foreign key to db.product_to_category.id.
    @type product_to_category_id: int
    @param kwargs: Relationship attributes in db.product_to_category.fields.
    @type kwargs: keywords.
    @return: True on succed, False otherwise.
    @rtype: bool
    """
    try:
        db.product_to_category[product_to_category_id] = kwargs
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True

def update_product_vendor(product_to_vendor_id, **kwargs):
    """
    Updates the product to vendor relationship. Return True on succed or
    False otherwise.

    @param product_to_vendor_id: Foreign key to db.product_to_vendor.id.
    @type product_to_vendor_id: int
    @param kwargs: Relationship attributes in db.product_to_vendor.fields.
    @type kwargs: keywords
    @return: True on succed, False otherwise.
    @rtype: bool
    """
    try:
        db.product_to_vendor[product_to_vendor_id] = kwargs
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True

def update_price_list(product_price_list_id, **kwargs):
    """
    Updates a product price list record. Return True on succed or False
    otherwise.
    @param product_price_list_id: Foreign key to db.product_price_lists.id.
    @type product_price_list_id: int
    @param kwargs: Price list attributes in db.product_to_vendor.fields.
    @type kwargs: keywords
    @return: True on succed, False otherwise.
    @rtype: bool
    """
    try:
        db.product_price_lists[product_price_list_id] = kwargs
    except Exception as e:
        db.rollback()
        return False
    else:
        db.commit()
        return True
