#
# Persistence class for Task.
# Usually, this should implement an interface that the domain layer provide. This approach will invert the dependency.
# And by using the strategy pattern, we can bind the interface to the class.
#

from todo import db
from todo.models import Task


class TaskPersistence():
    @staticmethod
    def read_all():
        return Task.query.all()

    @staticmethod
    def read_by_id(id):
        return Task.query.get_or_404(id)

    @staticmethod
    def create(**kwargs):
        t = Task(**kwargs)
        db.session.add(t)
        db.session.commit()

    @staticmethod
    def update(id, **kwargs):
        t = Task.query.get_or_404(id)
        t.title = kwargs['title']
        t.active = kwargs['active']
        db.session.commit()

    @staticmethod
    def delete(id):
        t = Task.query.get_or_404(id)
        db.session.delete(t)
        db.session.commit()