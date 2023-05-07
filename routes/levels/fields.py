from webargs import fields


create_level_model = {
    'text': fields.String(required=True),
}

delete_level_model = {
    'id': fields.Number(required=True),
}

edit_level_model = {
    'id': fields.Number(required=True),
    'text': fields.String(required=True),
}
