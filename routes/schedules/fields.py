from webargs import fields


create_schedule_model = {
    'date': fields.String(required=True),
}

remove_schedule_model = {
    'schedule_id': fields.Number(required=True),
}

edit_schedule_model = {
    'schedule_id': fields.Number(required=True),
    'date': fields.String(required=True),
}
