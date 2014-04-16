

import json

from django.http import HttpResponse
from django.contrib.sites.models import Site


def relative_to_fq_url(path):
    return 'http://{domain}{path}'.format(
        domain=Site.objects.get_current().domain,
        path=path,
    )


class JsonResponse(HttpResponse):
    def __init__(self, content='', content_type='application/json',
                 status=200):
        if not isinstance(content, str):
            content = json.dumps(content)

        super(JsonResponse, self).__init__(content=content, status=status,
                                           content_type=content_type)
