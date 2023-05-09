from flask import request
from exceptions import ApiError


def login_required(fn):
    def wrapper(*args, **kwargs):
        # password = request.cookies.get('account')
        # if not password:
        #     raise ApiError.UnauthorizedError()
        #
        # if password != hash('45330224'):
        #     raise ApiError.UnauthorizedError()

        return fn(123, *args, **kwargs)

    wrapper.__name__ = fn.__name__
    return wrapper
