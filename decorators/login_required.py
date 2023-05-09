from flask import request
from exceptions import ApiError
from models import Users


def login_required(fn):
    def wrapper(*args, **kwargs):
        user_session = request.cookies.get('session')
        if not user_session:
            raise ApiError.UnauthorizedError()

        user = Users.select().where(Users.session == user_session).get_or_none()
        if not user:
            raise ApiError.UnauthorizedError()

        return fn(user, *args, **kwargs)

    wrapper.__name__ = fn.__name__
    return wrapper
