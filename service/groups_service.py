from models import Groups
from exceptions import ApiError


def create(name: str, course: int):
    group = Groups(name=name, course=course)
    group.save()

    return group.get_dto()


def remove(group_id: int):
    group = Groups.delete().where(Groups.id == group_id)
    group.execute()


def edit(group_id: int, name: str, course: int):
    group = Groups.get_or_none(Groups.id == group_id)
    if not group:
        raise ApiError.BadRequest('Group not found')

    group.name = name
    group.course = course
    group.save()

    return group.get_dto()


def get_groups():
    return [group.get_dto() for group in Groups.select().order_by(Groups.course.asc())]


def get_group(group_id: int):
    group = Groups.get_or_none(Groups.id == group_id)
    if not group:
        raise ApiError.BadRequest('Group not found')

    return group.get_dto()
