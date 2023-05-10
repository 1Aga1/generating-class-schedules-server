from models import Groups
from exceptions import ApiError


def create(level_id: int, name: str):
    group = Groups(level_id=level_id, name=name)
    group.save()

    return group.get_dto()


def remove(group_id: int):
    group = Groups.delete().where(Groups.id == group_id)
    group.execute()


def edit(group_id: int, level_id: int, name: str):
    group = Groups.get_or_none(Groups.id == group_id)
    if not group:
        raise ApiError.BadRequest('Group not found')

    group.level = level_id
    group.name = name
    group.save()

    return group.get_dto()


def get_groups():
    return [group.get_dto() for group in Groups.select().order_by(Groups.level.asc())]


def get_group(group_id: int):
    group = Groups.get_or_none(Groups.id == group_id)
    if not group:
        raise ApiError.BadRequest('Group not found')

    return group.get_dto()
