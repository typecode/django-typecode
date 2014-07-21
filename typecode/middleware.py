

from django.contrib import admin


class LoginRequired(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if getattr(view_func, 'login_exempt', False):
            return None

        if not (request.user.is_authenticated() and request.user.is_staff):
            return admin.site.login(request,
                                    extra_context={'next': request.path})
