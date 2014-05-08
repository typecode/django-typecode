

from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.conf import settings


class AdminThumbImage(AdminFileWidget):

    thumbnail_options = {
        'crop': True,
        'size': (200, 200),
        'detail': True,
        'upscale': True
    }

    def render(self, name, value, attrs=None):
        out = []
        v = str(value)
        if v:
            thumb = value.get_thumbnail(self.thumbnail_options)
            thumb_path = settings.MEDIA_URL + str(thumb)
            out.append(u'<img src="%s" alt="%s thumbnail">' % (thumb_path, v))
        out.append(super(AdminThumbImage, self).render(name, value, attrs))
        return mark_safe(u''.join(out))
