from models import ScheduleParams


def add(schedule_id: int, group_id: int, subject_id: int):
    schedule_param = ScheduleParams(schedule_id=schedule_id, group_id=group_id, subject_id=subject_id)
    schedule_param.save()
    return schedule_param.get_dto()


def remove(schedule_param_id: int):
    schedule_param = ScheduleParams.delete().where(ScheduleParams.id == schedule_param_id)
    schedule_param.execute()
