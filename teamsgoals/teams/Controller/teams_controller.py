from teamsgoals.teams.Service.teams_service import TeamsService


class TeamController:

    def __init__(self, json_response):
        self.json_response = json_response

    def get_all_data_teams(self):
        try:
            team_service = TeamsService(json_response=self.json_response)
            self.json_response = team_service.get_data_teams()
        except Exception as error_logic:
            self.json_response['incidents'].append(error_logic)
        return self.json_response

    def get_data_teams_by_id(self, id_team):
        try:
            team_service = TeamsService(json_response=self.json_response)
            self.json_response = team_service.get_data_teams(id_team=id_team)
        except Exception as error_logic:
            self.json_response['incidents'].append(error_logic)
        return self.json_response

    def add_team(self, request):
        try:
            team_service = TeamsService(json_response=self.json_response)
            self.json_response = team_service.add_team(request=request)
        except Exception as error_logic:
            self.json_response['incidents'].append(error_logic)
        return self.json_response

    def update_data_teams(self, id_team, request):
        try:
            team_service = TeamsService(json_response=self.json_response)
            self.json_response = team_service.update_team(request=request, id_team=id_team)
        except Exception as error_logic:
            self.json_response['incidents'].append(error_logic)
        return self.json_response

    def delete_team(self, id_team):
        try:
            team_service = TeamsService(json_response=self.json_response)
            self.json_response = team_service.delete_team(id_team=id_team)
        except Exception as error_logic:
            self.json_response['incidents'].append(error_logic)
        return self.json_response
