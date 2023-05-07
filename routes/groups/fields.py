from webargs import fields


groups_add_model = {
    'level_id': fields.Number(required=True),
    'name': fields.String(required=True),
}

groups_remove_model = {
    'group_id': fields.Number(required=True),
}

groups_edit_model = {
    'group_id': fields.Number(required=True),
    'level_id': fields.Number(required=True),
    'name': fields.String(required=True),
}

