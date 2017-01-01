import functools
from flask import jsonify


def json(f):
    """Generate a JSON response from a Python dictionary."""
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        # Invoke the wrapped function
        rv = f(*args, **kwargs)

        # The wrapped function can return the dictionary alone, or can also include a status code and/or headers.
        # Here I separate all these items
        status = None
        headers = None
        if isinstance(rv, tuple):
            rv, status, headers = rv + (None,) * (3 - len(rv))
        if isinstance(status, (dict, list)):
            headers, status = status, None

        # Generate the JSON response
        rv = jsonify(rv)
        if status is not None:
            rv.status_code = status
        if headers is not None:
            rv.headers.extend(headers)
        return rv
    return wrapped
