from models import ScheduleParams, Subjects, Schedules, Groups
from exceptions import ApiError


def add(schedule_id: int, group_id: int, subject_id: int, number: int):
    schedule = Schedules.get_or_none(id=schedule_id)
    if not schedule:
        raise ApiError.BadRequest('Schedule not found')

    group = Groups.get_or_none(id=group_id)
    if not group:
        raise ApiError.BadRequest('Group not found')

    subject = Subjects.get_or_none(id=subject_id)
    if not subject:
        raise ApiError.BadRequest('Subject not found')

    schedule_param = ScheduleParams.select(ScheduleParams).join(Subjects)\
        .where(ScheduleParams.schedule == schedule_id, Subjects.office == subject.office,
               ScheduleParams.number == number)
    if schedule_param:
        raise ApiError.BadRequest('Office already set to another group')

    schedule_param = ScheduleParams(schedule=schedule_id, group=group_id, subject=subject_id, number=number)
    schedule_param.save()
    return schedule_param.get_dto()


def remove(schedule_id: int, group_id: int, subject_id: int, number: int):
    schedule_param = ScheduleParams.delete().where(ScheduleParams.schedule == schedule_id,
                                                   ScheduleParams.group == group_id,
                                                   ScheduleParams.subject == subject_id,
                                                   ScheduleParams.number == number,
                                                   )
    schedule_param.execute()
