from models import Levels
from exceptions import ApiError


def create(text: str):
    level = Levels(text=text)
    level.save()

    return level.get_dto()


def delete(level_id: int):
    level = Levels.delete().where(Levels.id == level_id)
    level.execute()


def edit(level_id: int, text: str):
    level = Levels.get_or_none(Levels.id == level_id)
    if not level:
        raise ApiError.BadRequest('Level not found')

    level.text = text
    level.save()

    return level.get_dto()


def get_levels():
    return [level.get_dto() for level in Levels.select()]


def get_level(level_id: int):
    level = Levels.get_or_none(Levels.id == level_id)
    if not level:
        raise ApiError.BadRequest('Level not found')

    return level.get_dto()
