from flask import Blueprint, request, jsonify, Response
from webargs import flaskparser

from decorators import login_required
from .fields import create_teachers_model, delete_teachers_model, edit_teachers_model
from service import teacher_sevice

teachers_router = Blueprint('teachers', __name__)


@teachers_router.post('/teacher/create')
@login_required
def create(user):
    data = flaskparser.parser.parse(create_teachers_model, request)
    level = teacher_sevice.create(data['fullname'])
    return jsonify(level)


@teachers_router.delete('/teacher/remove')
@login_required
def remove(user):
    data = flaskparser.parser.parse(delete_teachers_model, request)
    teacher_sevice.delete(data['teacher_id'])
    return Response(status=204)


@teachers_router.post('/teacher/edit')
@login_required
def edit(user):
    data = flaskparser.parser.parse(edit_teachers_model, request)
    level = teacher_sevice.edit(data['teacher_id'], data['fullname'])
    return jsonify(level)


@teachers_router.get('/teachers')
def get_subjects():
    subjects = teacher_sevice.get_teachers()
    return jsonify(subjects)


@teachers_router.get('/teacher/<teacher_id>')
def get_subject(teacher_id):
    subject = teacher_sevice.get_teacher(teacher_id)
    return jsonify(subject)

