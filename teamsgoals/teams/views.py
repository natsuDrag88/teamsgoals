from rest_framework.decorators import api_view

from teamsgoals.Util.response_service import ResponseService
from teamsgoals.teams.Controller.teams_controller import TeamController


@api_view(['POST', 'GET'])
def get_data_teams(request):
    _json_response = {'incidents': [], 'result': []}
    teams_controller = TeamController(json_response=_json_response)
    if request.method == "GET":
        json_data_teams = teams_controller.get_all_data_teams()
    else:
        json_data_teams = teams_controller.add_team(request=request)
    response = ResponseService(json_response=json_data_teams, request=request)
    return response.get_response()


@api_view(['PUT', 'GET', 'DELETE'])
def get_data_teams_by_id(request, id_team=None):
    _json_response = {'incidents': [], 'result': []}
    teams_controller = TeamController(json_response=_json_response)
    if request.method == "GET":
        json_data_teams = teams_controller.get_data_teams_by_id(id_team=id_team)
    elif request.method == "PUT":
        json_data_teams = teams_controller.update_data_teams(id_team=id_team, request=request)
    else:
        json_data_teams = teams_controller.delete_team(id_team=id_team)
    response = ResponseService(json_response=json_data_teams, request=request)
    return response.get_response()

