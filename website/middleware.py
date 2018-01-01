__author__ = 'adonis'

from django.contrib import messages


class ProductionServer(object):
    """Adds boolean production to request objects

    Value will be True if accessed from BCDF URL"""

    WARNING_MESSAGE = "On development server. Unpublished articles are visible"

    @classmethod
    def process_request(cls, request):
        host = request.get_host()
        if 'bovellcancerdiabetesfoundation.org' in host or \
                'bovellfoundation.org' in host:
            request.production = True
        elif 'localhost' in host:
            request.production = False
        else:
            request.production = False
        if not request.production:
            storage = messages.get_messages(request)
            warning = False
            for message in storage:
                if message.message == ProductionServer.WARNING_MESSAGE:
                    warning = True
                    break
            if not warning:
                messages.warning(request, ProductionServer.WARNING_MESSAGE)
            storage.used = False
        return None
