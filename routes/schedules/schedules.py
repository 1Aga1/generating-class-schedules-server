from flask import Response, request, Blueprint, jsonify
from webargs import flaskparser
from decorators import login_required
from service import schedules_service
from .fields import create_schedule_model, remove_schedule_model, edit_schedule_model, change_visibility_model


schedules_router = Blueprint('schedules', __name__)


@schedules_router.post('/schedule/create')
@login_required
def create(user):
    data = flaskparser.parser.parse(create_schedule_model, request)
    schedule = schedules_service.create(data['date'])
    return jsonify(schedule)


@schedules_router.delete('/schedule/remove')
@login_required
def remove(user):
    data = flaskparser.parser.parse(remove_schedule_model, request)
    schedules_service.remove(data['schedule_id'])
    return Response(status=204)


@schedules_router.post('/schedule/edit')
@login_required
def edit(user):
    data = flaskparser.parser.parse(edit_schedule_model, request)
    schedule = schedules_service.edit(data['schedule_id'], data['date'])
    return jsonify(schedule)


@schedules_router.get('/schedules')
def get_schedules():
    schedules = schedules_service.get_schedules()
    return jsonify(schedules)


@schedules_router.get('/schedule/<schedule_id>')
def get_schedule(schedule_id):
    schedule = schedules_service.get_schedule(schedule_id)
    return jsonify(schedule)


@schedules_router.post('/schedule/upload')
@login_required
def upload_schedule(user):
    file = request.files['file']

    return schedules_service.upload_schedule(file)

@schedules_router.post('/schedule/change_visibility')
@login_required
def change_visibility(user):
    data = flaskparser.parser.parse(change_visibility_model, request)
    schedule = schedules_service.change_visibility(data['schedule_id'], data['visible'])
    return jsonify(schedule)

@schedules_router.get('/schedules/urtk')
def urtk_schedules():
    schedules = schedules_service.urtk_schedules()
    return jsonify(schedules)
