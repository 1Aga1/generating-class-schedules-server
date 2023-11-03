import datetime
import io
import os
import xlsxwriter

from openpyxl import load_workbook
from werkzeug import Response

from models import Schedules, ScheduleParams, GroupSubjects, Groups, Subjects, Teachers
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
                group_name = sheet.cell(row=1, column=column).value

                group = Groups.get_or_none(course=int(group_name[0]), name=group_name)
                if not group:
                    group = Groups(course=int(group_name[0]), name=group_name)
                    group.save()

                for row in range(2, sheet.max_row+1):
                    cell_value = sheet.cell(row=row, column=column).value

                    if cell_value:
                        subjects = cell_value.split('/')

                        for data in subjects:
                            subject_w_teacher_w_office = data.split('-')
                            if subject_w_teacher_w_office[0] and subject_w_teacher_w_office[1] \
                                    and subject_w_teacher_w_office[2]:
                                teacher_fullname = subject_w_teacher_w_office[1]

                                teacher = Teachers.get_or_none(fullname=teacher_fullname)
                                if not teacher:
                                    teacher = Teachers(fullname=teacher_fullname)
                                    teacher.save()

                                subject = Subjects.get_or_none(name=subject_w_teacher_w_office[0],
                                                               teacher=teacher)
                                if not subject:
                                    subject = Subjects(name=subject_w_teacher_w_office[0],
                                                       teacher=teacher)
                                    subject.save()

                                group_subject = GroupSubjects.get_or_none(group=group, subject=subject)
                                if not group_subject:
                                    group_subject = GroupSubjects(group=group, subject=subject)
                                    group_subject.save()

                                schedule_param = ScheduleParams(schedule=schedule['id'], group=group, subject=subject,
                                                                number=row-1, office=subject_w_teacher_w_office[2])
                                schedule_param.save()

    return Response(status=200)


def change_visibility(schedule_id: int, visible: bool):
    schedule = Schedules.get_or_none(Schedules.id == schedule_id)
    if not schedule:
        raise ApiError.BadRequest('Schedule not found')

    schedule.visible = visible
    schedule.save()

    return schedule.get_dto()


def urtk_schedules():
    weekdays_en_ru = {
        'Monday': 'Понедельник',
        'Tuesday': 'Вторник',
        'Wednesday': 'Среда',
        'Thursday': 'Четверг',
        'Friday': 'Пятница',
        'Saturday': 'Суббота',
        'Sunday': 'Воскресенье',
    }

    urtk_schedules = {
        'lessonNumber': 6,
        'courses': []
    }

    schedules = Schedules.select().where(Schedules.visible == True).order_by(Schedules.date.asc())

    urtk_schedules = {
        'dates': [schedule.date.strftime("%d.%m.%Y") for schedule in schedules],
        'lessonNumber': 6,
        'courses': []
    }

    for course in range(1, 5):
        course_obj = {
            'name': course,
            'groups': []
        }

        groups = Groups.select().where(Groups.course == course)

        for group in groups:
            group_obj = {
                'name': group.name,
                'schedule': []
            }

            for schedule in schedules:
                schedule_params = ScheduleParams.select().where(ScheduleParams.schedule == schedule and
                                                               ScheduleParams.group == group)\
                                .order_by(ScheduleParams.number.asc())

                day = {
                    'date': schedule.date.strftime("%d.%m.%Y"),
                    'day': weekdays_en_ru[schedule.date.strftime("%A")],
                    'lessons': []
                }

                for index, param in enumerate(schedule_params):
                    subject = Subjects.get_or_none(Subjects.id == param.subject).get_dto()
                    if index > 0 and param.number == schedule_params[index].number:
                        day['lessons'][param.number-1]['lessonName'] += f'\n{subject["name"]} {subject["teacher"]["fullname"]}'
                        day['lessons'][param.number - 1]['office'] += f'/{param.office}'
                    else:
                        day['lessons'].append({
                            'lessonName': f'{subject["name"]} {subject["teacher"]["fullname"]}',
                            'office': f'{param.office}'
                        })

                group_obj['schedule'].append(day)

            course_obj['groups'].append(group_obj)

        urtk_schedules['courses'].append(course_obj)

    return urtk_schedules


def urtk_schedules_download():
    document_name = 'Расписание.xlsx'
    workbook = xlsxwriter.Workbook(document_name)

    urtk_schedule = urtk_schedules()

    with workbook:
        default_cell_format = workbook.add_format()
        default_cell_format.set_align('center')
        default_cell_format.set_align('vcenter')
        default_cell_format.set_text_wrap()
        default_cell_format.set_border()

        bold_format = workbook.add_format()
        bold_format.set_bold()
        for course in urtk_schedule['courses']:
            worksheet = workbook.add_worksheet(f'{course["name"]} курс')
            worksheet.merge_range(0, 0, 0, len(urtk_schedule['courses'])*3+1,
                                  f'Расписание занятий групп {course["name"]} курса на '
                                  f'{urtk_schedule["dates"][0]} - {urtk_schedule["dates"][len(urtk_schedule["dates"])]} '
                                  f'{urtk_schedule["dates"][0].split(".")[2]} года')
            row = 1
            col = 1
            for group in course['groups']:
                pass


    file_stream = io.BytesIO()
    workbook.save(file_stream)
    file_stream.seek(0)

    return file_stream, document_name

# https://xlsxwriter.readthedocs.io/worksheet.html
