#
# Here are the task endpoint
#

from flask import jsonify, request

from . import api

from todo.persistence.task import TaskPersistence
from todo.json_mappers.task_json import TaskJson
from todo.validators.task_validator import TaskValidator

from todo.decorators import json


@api.route('/tasks', methods=['GET'])
@api.route('/tasks/', methods=['GET'])
@json
def get_all_tasks():
    """Return all tasks"""
    return TaskJson.json_all()

@api.route('/tasks/<int:id>', methods=['GET'])
@api.route('/tasks/<int:id>/', methods=['GET'])
@json
def get_task_by_id(id):
    """Return task by its ID"""
    return TaskJson.json_by_id(id)

@api.route('/tasks', methods=['POST'])
@api.route('/tasks/', methods=['POST'])
@json
def create_task():
    """Create a new task"""
    data = request.get_json()

    # In advanced solution, a generic validation should be done
    if (TaskValidator._validate_title(data)):
        TaskPersistence.create(title=data['title'])
        return {'success': True, 'message': 'Task has been saved'}

    # Simple error response
    return {'error': 'bad request', 'message': 'not valid data', 'status': 400}

@api.route('/tasks/<int:id>', methods=['PUT'])
@api.route('/tasks/<int:id>/', methods=['PUT'])
@json
def update_task(id):
    """Update an existing task by its ID"""
    data = request.get_json()

    # In advanced solution, a generic validation should be done
    if (TaskValidator._validate_title(data) and TaskValidator._validate_active(data)):
        TaskPersistence.update(id, title=data['title'], active=data['active'])
        return {'success': True, 'message': 'Task has been updated'}

    # Simple error response
    return {'error': 'bad request', 'message': 'not valid data', 'status': 400}

@api.route('/tasks/<int:id>', methods=['DELETE'])
@api.route('/tasks/<int:id>/', methods=['DELETE'])
@json
def delete_task(id):
    """Delete a task by its ID"""
    TaskPersistence.delete(id)
    return {'success': True, 'message': 'Task has been deleted'}

