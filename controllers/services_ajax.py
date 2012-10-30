# -*- coding: utf-8 -*-

@auth.requires_login()
def create_service():
    id = None
    data = dict()
    data_description = dict()
    vars = request.vars

    data['alternative_code'] = vars.alternative_code.decode('utf-8').upper()
    data['part_number'] = vars.part_number.decode('utf-8').upper()
    data['serial_number'] = vars.serial_number.decode('utf-8').upper()
    data['model'] = vars.model.decode('utf-8').upper()
    data['standard_cost'] = vars.standard_cost
    data['markup'] = vars.markup

    data_description['name'] = vars.name.decode('utf-8').upper()
    data_description['alternative_name'] = vars.alternative_name.decode('utf-8').upper()
    data_description['description'] = vars.description.decode('utf-8').upper()

    try:
        id = db.services.insert(**data)
        if id:
            data_description['service_id'] = id
            db.service_descriptions.insert(**data_description)
    except SyntaxError as e:
        db.rollback()
        if 'duplicate field' in e:
            return 0
        else:
            return ''
    except Exception as e:
        db.rollback()
        return ''
    else:
        try:
            code = 'SERV{}'.format(id)
            result = db(db.services.id==id).update(code=code)
        except Exception as e:
            db.rollback()
            return ''
        else:
            if result==1:
                db.commit()
                return str(id)
            else:
                db.rollback()
                return ''

@auth.requires_login()
def get_services():
    pass

@auth.requires_login()
def get_service_information():
    pass

@auth.requires_login()
def update_service():
    pass

@auth.requires_login()
def toggle_service():
    pass
