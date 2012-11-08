# -*- coding: utf-8 -*-

@auth.requires_membership('GOD', 'Almacenista')
def create_entry():
    data = dict()
    v = request.vars
    received_by = session.selected_user.id
    session.selected_user = None

    if v.branch_id and  v. warehouse_id:
        return ''
    if v.branch_id:
        data['branch_id'] = v.branch_id
        data['warehouse_id'] = None
    if v.warehouse_id:
        data['warehouse_id'] = v.warehouse_id
        data['branch_id'] = None

    data['reference'] = v.reference
    data['description'] = v.description
    data['concept_id'] = v.concept_id
    data['date_receipt'] = v.date_receipt
    data['received_by'] = session.received_id
    return str(received_by)
