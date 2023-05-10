from models import Schedules, ScheduleParams
from exceptions import ApiError


def create(date: str):
    schedule = Schedules(date=date)
    schedule.save()
    return schedule.get_dto()


def remove(schedule_id: int):
    schedule = Schedules.delete().where(Schedules.id == schedule_id)
    schedule.execute()


def edit(schedule_id: int, date: str):
    schedule = Schedules.get_or_none(Schedules.id == schedule_id)
    if not schedule:
        raise ApiError.BadRequest('Schedule not found')

    schedule.date = date
    schedule.save()

    return schedule.get_dto()


def get_schedules():
    return [schedule.get_dto() for schedule in Schedules.select().order_by(Schedules.date.asc())]


def get_schedule(schedule_id: int):
    schedule = Schedules.get_or_none(Schedules.id == schedule_id)
    if not schedule:
        raise ApiError.BadRequest('Schedule not found')

    return {
        **schedule.get_dto(),
        'params': [param.get_dto() for param in ScheduleParams.select().where(ScheduleParams.schedule == schedule).order_by(ScheduleParams.number.asc())]
    }
