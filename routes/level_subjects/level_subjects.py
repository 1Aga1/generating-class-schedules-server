from flask import Blueprint, request, jsonify, Response
from webargs import flaskparser

from decorators import login_required
from .fields import level_subjects_add_model, level_subjects_remove_model
from service import level_subjects_service


level_subjects_router = Blueprint('level_subjects', __name__)


@level_subjects_router.post('/level_subjects/add')
@login_required
def add(password):
    data = flaskparser.parser.parse(level_subjects_add_model, request)
    level_subjects = level_subjects_service.add(data['level_id'], data['subject_id'])
    return jsonify(level_subjects)


@level_subjects_router.delete('/level_subjects/remove')
@login_required
def remove(password):
    data = flaskparser.parser.parse(level_subjects_remove_model, request)
    level_subjects_service.remove(data['level_id'], data['subject_id'])
    return Response(status=204)


@level_subjects_router.get('/level_subjects/<level_id>')
def get_level_subjects(level_id):
    level_subjects = level_subjects_service.get_level_subjects(level_id)
    return jsonify(level_subjects)
