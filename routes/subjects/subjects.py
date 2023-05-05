from flask import Blueprint, request, jsonify, Response
from webargs import flaskparser
from .fields import create_subjects_model, delete_subjects_model, edit_subjects_model
from service import subjects_service

subjects_router = Blueprint('subjects', __name__)


@subjects_router.post('/subject/create')
def create():
    data = flaskparser.parser.parse(create_subjects_model, request)
    level = subjects_service.create(data['name'], data['office'])
    return jsonify(level)


@subjects_router.delete('/subject/remove')
def remove():
    data = flaskparser.parser.parse(delete_subjects_model, request)
    subjects_service.delete(data['id'])
    return Response(status=204)


@subjects_router.post('/subject/edit')
def edit():
    data = flaskparser.parser.parse(edit_subjects_model, request)
    level = subjects_service.edit(data['id'], data['name'], data['office'])
    return jsonify(level)


@subjects_router.get('/subjects')
def get_levels():
    levels = subjects_service.get()
    return jsonify(levels)

