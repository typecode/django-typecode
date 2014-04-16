

from django.conf import settings


def build(request):
    if not hasattr(settings, 'BUILD_NUMBER'):
        return {}

    return {'BUILD_NUMBER': settings.BUILD_NUMBER}
