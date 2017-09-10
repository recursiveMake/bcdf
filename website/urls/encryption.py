from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns(
    '',
    # /challenge-slug
    url(r'^(?P<challenge_slug>.+)$', views.encryption_challenge, name='challenge'),
)
