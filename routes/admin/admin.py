from flask import Blueprint, make_response
from exceptions import ApiError


admin_router = Blueprint('admin', __name__)


@admin_router.post('/admin/<password>')
def login(password):
    if password != 45330224:
        raise ApiError.BadRequest('Incorrect password')
    res = make_response('success')
    res.set_cookie('account', str(hash(password)), max_age=60 * 60 * 24)

    return res


@admin_router.post('/logout')
def logout():
    res = make_response('success')
    res.set_cookie('account', '', max_age=0)

    return res
