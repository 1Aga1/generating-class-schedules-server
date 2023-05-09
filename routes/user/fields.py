from webargs import fields


login_model = {
    'username': fields.String(required=True),
    'password': fields.String(required=True),
}