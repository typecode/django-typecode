

from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.staticfiles.storage import staticfiles_storage as ss

from typecode.utils import relative_to_fq_url


DEFAULT_TYPE = getattr(settings, 'OPENGRAPH_DEFAULT_TYPE', 'website')

DEFAULT_LOCALE = getattr(settings, 'OPENGRAPH_DEFAULT_LOCALE', 'en_US')

DEFAULT_TITLE = getattr(settings, 'OPENGRAPH_DEFAULT_TITLE', Site.objects.get_current().name)

DEFAULT_DESCRIPTION = getattr(settings, 'OPENGRAPH_DEFAULT_DESCRIPTION', '')

if hasattr(settings, 'OPENGRAPH_DEFAULT_IMAGE'):
    DEFAULT_IMAGE = relative_to_fq_url(ss.url(settings.OPENGRAPH_DEFAULT_IMAGE))
else:
    DEFAULT_IMAGE = None


def opengraph(request):
    default = {
        'type': DEFAULT_TYPE,
        'locale': DEFAULT_LOCALE,
        'site_name': DEFAULT_TITLE,
        'title': DEFAULT_TITLE,
        'description': DEFAULT_DESCRIPTION,
        'url': relative_to_fq_url(''),
        'images': []
    }
    if DEFAULT_IMAGE:
        default['images'].append(DEFAULT_IMAGE)

    obj = getattr(request, 'opengraph', None)
    if obj and hasattr(obj, 'get_opengraph'):
        og = obj.get_opengraph()
        for k, v in og.items():
            if not v:
                del og[k]

        default.update(og)

    return {
        'opengraph': default
    }
