

from django.contrib import admin


class LoginRequired(object):
    def process_request(self, request):
        if not (request.user.is_authenticated() and request.user.is_staff):
            return admin.site.login(request,
                                    extra_context={'next': request.path})
