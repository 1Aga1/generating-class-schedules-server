from webargs import fields


groups_create_model = {
    'name': fields.String(required=True),
    'course': fields.Number(required=True),
}

groups_remove_model = {
    'group_id': fields.Number(required=True),
}

groups_edit_model = {
    'group_id': fields.Number(required=True),
    'name': fields.String(required=True),
    'course': fields.Number(required=True),
}

