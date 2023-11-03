from flask import Blueprint, request, jsonify, Response
from service import schedule_params_service
from webargs import flaskparser
from decorators import login_required
from .fields import schedule_param_add_model, schedule_param_remove_model


schedule_params_router = Blueprint('schedule_params', __name__)


@schedule_params_router.post('/schedule_param/add')
@login_required
def add(user):
    data = flaskparser.parser.parse(schedule_param_add_model, request)
    schedule_param = schedule_params_service.add(data['schedule_id'], data['group_id'], data['sub_group'], data['subject_id'],
                                                 data['first_half'], data['number'], data['office'])
    return jsonify(schedule_param)


@schedule_params_router.delete('/schedule_param/remove')
@login_required
def remove(user):
    data = flaskparser.parser.parse(schedule_param_remove_model, request)
    schedule_params_service.remove(data['schedule_id'], data['group_id'], data['subject_id'], data['number'])
    return Response(status=204)

