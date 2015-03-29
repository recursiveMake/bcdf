__author__ = 'adonis'

from django.contrib import messages


class ProductionServer(object):
    """Adds boolean production to request objects

    Value will be True if accessed from BCDF URL"""

    @classmethod
    def process_request(cls, request):
        host = request.get_host()
        if 'bovellcancerdiabetesfoundation.org' in host or \
                'bovellfoundation.org' in host:
            request.production = True
        elif 'web-bcdf.rhcloud.com' in host:
            request.production = False
        elif 'localhost' in host:
            request.production = False
        else:
            request.production = False
        if not request.production:
            messages.warning(request, "On development server. Unpublished articles are visible")
        return None