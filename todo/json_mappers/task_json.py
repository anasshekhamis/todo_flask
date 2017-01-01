#
# Provide the structure of the returned JSON
#

import calendar

from todo.persistence.task import TaskPersistence

class TaskJson(object):
    @staticmethod
    def json_all():
        return {'tasks': [{'id': task.id, 'title': task.title, 'active': task.active} for task in TaskPersistence.read_all()]}

    @staticmethod
    def json_by_id(id):
        t = TaskPersistence.read_by_id(id)
        return {'task': {'id': t.id,'title': t.title, 'active': t.active, 'created_at': calendar.timegm(t.created_at.utctimetuple()), 'updated_at': calendar.timegm(t.updated_at.utctimetuple())}}