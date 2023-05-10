from models import ScheduleParams


def add(schedule_id: int, group_id: int, subject_id: int, number: int):
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
