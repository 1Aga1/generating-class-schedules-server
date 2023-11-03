from webargs import fields


schedule_param_add_model = {
    'schedule_id': fields.Number(required=True),
    'group_id': fields.Number(required=True),
    'sub_group': fields.String(required=False, load_default=None),
    'subject_id': fields.Number(required=True),
    'first_half': fields.String(required=False, load_default=None),
    'number': fields.Number(required=True),
    'office': fields.String(required=True)
}

schedule_param_remove_model = {
    'schedule_id': fields.Number(required=True),
    'group_id': fields.Number(required=True),
    'subject_id': fields.Number(required=True),
    'number': fields.Number(required=True),
}
