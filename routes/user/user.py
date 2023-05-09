from flask import Blueprint, make_response, request, jsonify, Response
from webargs import flaskparser

from exceptions import ApiError
from service import user_service
from .fields import login_model


user_router = Blueprint('user', __name__)


@user_router.post('/user/login')
def login():
    data = flaskparser.parser.parse(login_model, request)
    user, session = user_service.login(data['username'], data['password'])

    res = make_response(jsonify(user))
    res.set_cookie('session', session)

    return res


@user_router.post('/user/logout')
def logout():
    res = make_response(Response(status=200))
    res.set_cookie('session', '')

    return res


@user_router.get('/user/checkout')
def checkout():
    session = request.cookies.get('session')
    if not session:
        raise ApiError.UnauthorizedError()

    user = user_service.checkout(session)
    return jsonify(user)
