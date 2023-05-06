from flask import Blueprint, request, jsonify, Response
from webargs import flaskparser
from fields import group_subjects_add_model, group_subjects_remove_model
from service import group_subjects_service


group_subjects_router = Blueprint('group_subjects', __name__)


@group_subjects_router.post('/group_subject/add')
def add():
    data = flaskparser.parser.parse(group_subjects_add_model, request)
    group_subject = group_subjects_service.add(data['group_id'], data['subject_id'])
    return jsonify(group_subject)


@group_subjects_router.delete('/group_subject/remove')
def remove():
    data = flaskparser.parser.parse(group_subjects_remove_model, request)
    group_subjects_service.remove(data['group_id'], data['subject_id'])
    return Response(status=204)


@group_subjects_router.get('/group_subjects')
def get():
    group_subjects = group_subjects_service.get()
    return jsonify(group_subjects)
