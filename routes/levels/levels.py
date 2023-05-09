from flask import Blueprint, request, jsonify, Response
from webargs import flaskparser

from decorators import login_required
from .fields import create_level_model, delete_level_model, edit_level_model
from service import levels_service

level_router = Blueprint('levels', __name__)


@level_router.post('/level/create')
@login_required
def create(password):
    data = flaskparser.parser.parse(create_level_model, request)
    level = levels_service.create(data['text'])
    return jsonify(level)


@level_router.delete('/level/remove')
@login_required
def remove(password):
    data = flaskparser.parser.parse(delete_level_model, request)
    levels_service.delete(data['level_id'])
    return Response(status=204)


@level_router.post('/level/edit')
@login_required
def edit(password):
    data = flaskparser.parser.parse(edit_level_model, request)
    level = levels_service.edit(data['level_id'], data['text'])
    return jsonify(level)


@level_router.get('/levels')
def get_levels():
    levels = levels_service.get_levels()
    return jsonify(levels)


@level_router.get('/level/<level_id>')
def get_level(level_id):
    levels = levels_service.get_level(level_id)
    return jsonify(levels)

