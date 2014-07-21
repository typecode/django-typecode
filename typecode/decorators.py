

from functools import wraps

from django.utils.decorators import available_attrs


def login_exempt(view_func):
    '''
    Marks a view function as being exempt from requiring login
    '''
    def wrapped_view(*args, **kwargs):
        return view_func(*args, **kwargs)
    wrapped_view.login_exempt = True
    return wraps(view_func, assigned=available_attrs(view_func))(wrapped_view)
