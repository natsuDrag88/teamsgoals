from rest_framework import routers
from django.conf.urls import include, url

from teamsgoals.teams.views import get_data_teams, get_data_teams_by_id

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^v1/teams/$', get_data_teams, name='get_data_teams'),
    url(r'^v1/teams/(?P<id_team>\w*)/$', get_data_teams_by_id, name='get_data_teams_by_id'),
]
