from teamsgoals.player.Repository.player_repository import PlayerRepository
from teamsgoals.teams.Repository.teams_repository import TeamsRepository


class TeamsService:

    def __init__(self, json_response):
        self.json_response = json_response
        self.teams_repository = TeamsRepository()
        self.player_repository = PlayerRepository()

    def get_data_teams(self, id_team=None):
        data_teams = self.teams_repository.get_info_team_by_id(id_team=id_team) if id_team else \
            self.teams_repository.get_info_teams_all()
        if data_teams:
            self.get_json_response(data_teams=data_teams)
        else:
            self.json_response['incidents'].append('No data to display')
        return self.json_response

    def get_json_response(self, data_teams):
        for team in data_teams:
            sum_goals = self.player_repository.get_sum_goals(team.id)
            self.json_response['result'].append({
                'teams_id': team.id,
                'name': team.name,
                'city': team.city,
                'goals_count': sum_goals['goals__sum'] if sum_goals['goals__sum'] else 0
            })

    def add_team(self, request):
        # noinspection PyBroadException
        try:
            if request.data['name'] and request.data['city']:
                self.teams_repository.add_team(name=request.data['name'], city=request.data['city'])
                self.json_response['result'] = 'The record was entered correctly.'
            else:
                self.json_response['incidents'].append('Expected parameters were not provided.')
        except Exception:
            self.json_response['incidents'].append('An error occurred while inserting the record.')
        return self.json_response

    def update_team(self, request, id_team):
        # noinspection PyBroadException
        try:
            data_team = self.teams_repository.get_info_team_by_id_object(id_team=id_team)
            if data_team:
                self.teams_repository.update_team(request=request, team=data_team)
                self.json_response['result'] = 'The record has been successfully updated.'
            else:
                self.json_response['incidents'].append('The team to look for does not exist')
        except Exception:
            self.json_response['incidents'].append('An error occurred while updating the registry.')
        return self.json_response

    def delete_team(self, id_team):
        # noinspection PyBroadException
        try:
            data_team = self.teams_repository.get_info_team_by_id_object(id_team=id_team)
            if data_team:
                self.teams_repository.delete_team(team=data_team)
                self.json_response['result'] = 'The record has been deleted successfully.'
            else:
                self.json_response['incidents'].append('The team to look for does not exist')
        except Exception:
            self.json_response['incidents'].append('An error occurred while deleting the record.')
        return self.json_response
