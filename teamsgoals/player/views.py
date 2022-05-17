from rest_framework.decorators import api_view

from teamsgoals.Util.response_service import ResponseService
from teamsgoals.player.Controller.players_controller import PlayersController


@api_view(['POST', 'GET'])
def get_data_player(request):
    _json_response = {'incidents': [], 'result': []}
    player_controller = PlayersController(json_response=_json_response)
    if request.method == "GET":
        json_data_teams = player_controller.get_all_data_players()
    else:
        json_data_teams = player_controller.add_player(request=request)
    response = ResponseService(json_response=json_data_teams, request=request)
    return response.get_response()


@api_view(['PUT', 'GET', 'DELETE'])
def get_data_player_by_id(request, id_player=None):
    _json_response = {'incidents': [], 'result': []}
    player_controller = PlayersController(json_response=_json_response)
    if request.method == "GET":
        json_data_teams = player_controller.get_data_player_by_id(id_player=id_player)
    elif request.method == "PUT":
        json_data_teams = player_controller.update_data_player(id_player=id_player, request=request)
    else:
        json_data_teams = player_controller.delete_player(id_player=id_player)
    response = ResponseService(json_response=json_data_teams, request=request)
    return response.get_response()
