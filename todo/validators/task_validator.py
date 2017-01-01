#
# Simple validation.
# For advanced and more practical solution, should use a validation library.
#
class TaskValidator(object):

    @staticmethod
    def _validate_title(data):
        if 'title' in data.keys() and (type(data['title']) == str):
            return True
        return False

    @staticmethod
    def _validate_active(data):
        if 'active' in data.keys() and (type(data['active']) == bool):
            return True
        return False
