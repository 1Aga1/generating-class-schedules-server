from models import Teachers
from exceptions import ApiError


def create(fullname: str):
    teacher = Teachers(fullname=fullname)
    teacher.save()

    return teacher.get_dto()


def delete(teacher_id: int):
    teacher = Teachers.delete().where(Teachers.id == teacher_id)
    teacher.execute()


def edit(teacher_id: int, fullname: str):
    teacher = Teachers.get_or_none(Teachers.id == teacher_id)
    if not teacher:
        raise ApiError.BadRequest('Teacher not found')

    teacher.fullname = fullname
    teacher.save()

    return teacher.get_dto()


def get_teachers():
    return [teacher.get_dto() for teacher in Teachers.select().order_by(Teachers.fullname.asc())]


def get_teacher(teacher_id: int):
    teacher = Teachers.get_or_none(id=teacher_id)
    if not teacher:
        raise ApiError.BadRequest('Teacher not found')

    return teacher.get_dto()
