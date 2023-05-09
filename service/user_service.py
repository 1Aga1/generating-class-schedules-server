from models import Users
from exceptions import ApiError
from werkzeug.security import check_password_hash
from uuid import uuid4


def login(username: str, password: str):
    user = Users.get_or_none(username=username)
    if not user or check_password_hash(user.password, password):
        raise ApiError.BadRequest('Wrong username or password')

    session = str(uuid4())

    user.session = session
    user.save()

    return user.get_dto(), session


def checkout(session: str):
    user = Users.get_or_none(session=session)
    if not user:
        ApiError.UnauthorizedError()

    return user.get_dto()
