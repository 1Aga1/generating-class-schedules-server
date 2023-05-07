from flask import Blueprint, request, jsonify, Response
from service import schedule_params_service
from webargs import flaskparser
from .fields import schedule_param_add_model, schedule_param_remove_model


schedule_params_router = Blueprint('schedule_params', __name__)


@schedule_params_router.post('/schedule_param/add')
def add():
    data = flaskparser.parser.parse(schedule_param_add_model, request)
    schedule_param = schedule_params_service.add(data['schedule_id'], data['group_id'], data['subject_id'])
    return jsonify(schedule_param)


@schedule_params_router.delete('/schedule_param/remove')
def remove():
    data = flaskparser.parser.parse(schedule_param_remove_model, request)
    schedule_params_service.remove(data['schedule_param_id'])
    return Response(status=204)
