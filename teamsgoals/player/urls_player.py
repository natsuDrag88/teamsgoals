from rest_framework import routers
from django.conf.urls import include, url

from teamsgoals.player.views import get_data_player, get_data_player_by_id

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^v1/player/$', get_data_player, name='get_data_player'),
    url(r'^v1/player/(?P<id_player>\w*)/$', get_data_player_by_id, name='get_data_player_by_id'),
]
