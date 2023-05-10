from webargs import fields


schedule_param_add_model = {
    'schedule_id': fields.Number(required=True),
    'group_id': fields.Number(required=True),
    'subject_id': fields.Number(required=True),
}

schedule_param_remove_model = {
    **schedule_param_add_model
}
