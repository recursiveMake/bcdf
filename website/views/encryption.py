import json

from django.http import HttpResponse

from bcdf.settings import CHALLENGE_DATA_FILE


def encryption_challenge(request, challenge_slug):
    # host = request.META['HTTP_HOST']
    with open(CHALLENGE_DATA_FILE) as data_file:
        chanllenge_responses = json.loads(data_file.read())
    response = chanllenge_responses.get(challenge_slug, 'Unknown challenge.')
    return HttpResponse(
        content=response, content_type='text/plain'
    )
