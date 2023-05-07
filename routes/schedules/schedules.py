from flask import Response, request, Blueprint, jsonify
from webargs import flaskparser
from service import schedules_service
from .fields import create_schedule_model, remove_schedule_model, edit_schedule_model


schedules_router = Blueprint('schedules', __name__)


@schedules_router.post('/schedule/create')
def create():
    data = flaskparser.parser.parse(create_schedule_model, request)
    schedule = schedules_service.create(data['date'])
    return jsonify(schedule)


@schedules_router.delete('/schedule/remove')
def remove():
    data = flaskparser.parser.parse(remove_schedule_model, request)
    schedules_service.remove(data['schedule_id'])
    return Response(status=204)


@schedules_router.post('/schedule/edit')
def edit():
    data = flaskparser.parser.parse(edit_schedule_model, request)
    schedule = schedules_service.edit(data['schedule_id'], data['date'])
    return jsonify(schedule)


@schedules_router.get('/schedules')
def get_schedules():
    schedules = schedules_service.get_schedules()
    return jsonify(schedules)


@schedules_router.get('/schedule/<schedule_id>')
def get_schedules(schedule_id):
    schedule = schedules_service.get_schedule(schedule_id)
    return jsonify(schedule)
