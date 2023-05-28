import datetime
import os

from openpyxl import load_workbook
from werkzeug import Response

from models import Schedules, ScheduleParams, Levels, LevelSubjects, Groups, Subjects, Teachers
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


def upload_schedule(file):
    filename, file_extension = os.path.splitext(file.filename)
    if file_extension not in ['.xlsx', '.xls']:
        raise ApiError.BadRequest('Incorrect file format')

    work_book = load_workbook(file)

    for sheet_name in work_book.get_sheet_names():
        nigger = [int(item) for item in sheet_name.split('.')]
        schedule = create(datetime.date(nigger[2], nigger[1], nigger[0]).strftime('%Y-%m-%d'))

        sheet = work_book.get_sheet_by_name(sheet_name)

        for column in range(1, sheet.max_column + 1):

            if sheet.cell(row=1, column=column).value:
                level_text = sheet.cell(row=1, column=column).value

                level = Levels.get_or_none(text=level_text)
                if not level:
                    level = Levels(text=level_text)
                    level.save()

                group_name = sheet.cell(row=2, column=column).value

                group = Groups.get_or_none(level=level, name=group_name)
                if not group:
                    group = Groups(level=level, name=group_name)
                    group.save()

                for row in range(3, sheet.max_row+1):
                    cell_value = sheet.cell(row=row, column=column).value

                    if cell_value:
                        subjects = cell_value.split('/')

                        for data in subjects:

                            subject_w_teacher = data.split('!')
                            if len(subject_w_teacher) > 1:
                                teacher_fullname = subject_w_teacher[1]

                                teacher = Teachers.get_or_none(fullname=teacher_fullname)
                                if not teacher:
                                    teacher = Teachers(fullname=teacher_fullname)
                                    teacher.save()

                                subject_data = subject_w_teacher[0].split('-')
                                if len(subject_data) > 1:

                                    subject = Subjects.get_or_none(name=subject_data[0], office=subject_data[1],
                                                                   teacher=teacher)
                                    if not subject:
                                        subject = Subjects(name=subject_data[0], office=subject_data[1],
                                                           teacher=teacher)
                                        subject.save()

                            subject_data = subject_w_teacher[0].split('-')

                            subject = Subjects.get_or_none(name=subject_data[0], office=subject_data[1])
                            if subject:

                                level_subject = LevelSubjects.get_or_none(level=level, subject=subject)
                                if not level_subject:
                                    level_subject = LevelSubjects(level=level, subject=subject)
                                    level_subject.save()

                                schedule_param = ScheduleParams(schedule=schedule['id'], group=group, subject=subject,
                                                                number=row-2)
                                schedule_param.save()

    return Response(status=200)
