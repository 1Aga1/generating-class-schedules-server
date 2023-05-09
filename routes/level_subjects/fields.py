from webargs import fields


level_subjects_add_model = {
    'level_id': fields.Number(required=True),
    'subject_id': fields.Number(required=True),
}

level_subjects_remove_model = {
    **level_subjects_add_model
}
