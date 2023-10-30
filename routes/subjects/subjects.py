from flask import Blueprint, request, jsonify, Response
from webargs import flaskparser

from decorators import login_required
from .fields import create_subjects_model, delete_subjects_model, edit_subjects_model
from service import subjects_service

subjects_router = Blueprint('subjects', __name__)


@subjects_router.post('/subject/create')
@login_required
def create(user):
    data = flaskparser.parser.parse(create_subjects_model, request)
    level = subjects_service.create(data['name'], data['teacher_id'])
    return jsonify(level)


@subjects_router.delete('/subject/remove')
@login_required
def remove(user):
    data = flaskparser.parser.parse(delete_subjects_model, request)
    subjects_service.delete(data['subject_id'])
    return Response(status=204)


@subjects_router.post('/subject/edit')
@login_required
def edit(user):
    data = flaskparser.parser.parse(edit_subjects_model, request)
    level = subjects_service.edit(data['subject_id'], data['name'], data['teacher_id'])
    return jsonify(level)


@subjects_router.get('/subjects')
def get_subjects():
    subjects = subjects_service.get_subjects()
    return jsonify(subjects)


@subjects_router.get('/subject/<subject_id>')
def get_subject(subject_id):
    subject = subjects_service.get_subject(subject_id)
    return jsonify(subject)

