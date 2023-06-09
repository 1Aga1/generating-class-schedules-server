from models import Subjects
from exceptions import ApiError


def create(name: str, office: str, teacher_id: int):
    subject = Subjects(name=name, office=office, teacher=teacher_id)
    subject.save()

    return subject.get_dto()


def delete(subject_id: int):
    subject = Subjects.delete().where(Subjects.id == subject_id)
    subject.execute()


def edit(subject_id: int, name: str, office: str, teacher_id: int):
    subject = Subjects.get_or_none(Subjects.id == subject_id)
    if not subject:
        raise ApiError.BadRequest('Subject not found')

    subject.name = name
    subject.office = office
    subject.teacher = teacher_id
    subject.save()

    return subject.get_dto()


def get_subjects():
    return [subject.get_dto() for subject in Subjects.select().order_by(Subjects.name.asc())]


def get_subject(subject_id: int):
    subject = Subjects.get_or_none(id=subject_id)
    if not subject:
        raise ApiError.BadRequest('Subject not found')

    return subject.get_dto()
