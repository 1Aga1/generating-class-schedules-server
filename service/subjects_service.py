from models import Subjects
from exceptions import ApiError


def create(name: str, office: str):
    subject = Subjects(name=name, office=office)
    subject.save()

    return subject.get_dto()


def delete(subject_id: int):
    subject = Subjects.delete().where(Subjects.id == subject_id)
    subject.execute()


def edit(subject_id: int, name: str, office: str):
    subject = Subjects.get_or_none(Subjects.id == subject_id)
    if not subject:
        raise ApiError.BadRequest('Subject not found')

    subject.name = name
    subject.office = office
    subject.save()

    return subject


def get():
    return [subject.get_dto() for subject in Subjects.select()]
