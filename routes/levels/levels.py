from flask import Blueprint, request, jsonify, Response
from webargs import flaskparser
from .fields import create_level_model, delete_level_model, edit_level_model
from service import levels_service

level_router = Blueprint('levels', __name__)


@level_router.post('/level/create')
def create():
    data = flaskparser.parser.parse(create_level_model, request)
    level = levels_service.create(data['text'])
    return jsonify(level)


@level_router.delete('/level/remove')
def remove():
    data = flaskparser.parser.parse(delete_level_model, request)
    levels_service.delete(data['id'])
    return Response(status=204)


@level_router.post('/level/edit')
def edit():
    data = flaskparser.parser.parse(edit_level_model, request)
    level = levels_service.edit(data['id'], data['text'])
    return jsonify(level)


@level_router.get('/levels')
def get_levels():
    levels = levels_service.get()
    return jsonify(levels)

