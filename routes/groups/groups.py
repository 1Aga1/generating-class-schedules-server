from flask import Blueprint, request, jsonify, Response
from webargs import flaskparser
from decorators import login_required
from .fields import groups_create_model, groups_remove_model, groups_edit_model
from service import groups_service


groups_router = Blueprint('groups', __name__)


@groups_router.post('/group/create')
@login_required
def create(user):
    data = flaskparser.parser.parse(groups_create_model, request)
    group = groups_service.create(data['level_id'], data['name'])
    return jsonify(group)


@groups_router.delete('/group/remove')
@login_required
def remove(user):
    data = flaskparser.parser.parse(groups_remove_model, request)
    groups_service.remove(data['group_id'])
    return Response(status=204)


@groups_router.post('/group/edit')
@login_required
def edit(user):
    data = flaskparser.parser.parse(groups_edit_model, request)
    group = groups_service.edit(data['group_id'], data['level_id'], data['name'])
    return jsonify(group)


@groups_router.get('/groups')
def get_groups():
    groups = groups_service.get_groups()
    return jsonify(groups)


@groups_router.get('/group/<group_id>')
def get_group(group_id):
    group = groups_service.get_group(group_id)
    return jsonify(group)
