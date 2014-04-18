
from django.core.exceptions import PermissionDenied


class VisibilityObjectMixin(object):

    def get(self, request, *args, **kwargs):
        if not self.get_object().can_view(request.user):
            raise PermissionDenied
        return super(VisibilityObjectView, self).get(request, *args, **kwargs)
