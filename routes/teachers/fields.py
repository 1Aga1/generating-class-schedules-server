from webargs import fields


create_teachers_model = {
    'fullname': fields.String(required=True),
}

delete_teachers_model = {
    'teacher_id': fields.Number(required=True),
}

edit_teachers_model = {
    'teacher_id': fields.Number(required=True),
    'fullname': fields.String(required=True),
}
