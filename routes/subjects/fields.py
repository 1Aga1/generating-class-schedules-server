from webargs import fields


create_subjects_model = {
    'name': fields.String(required=True),
    'office': fields.String(required=True),
}

delete_subjects_model = {
    'subject_id': fields.Number(required=True),
}

edit_subjects_model = {
    'subject_id': fields.Number(required=True),
    'name': fields.String(required=True),
    'office': fields.String(required=True),
}
