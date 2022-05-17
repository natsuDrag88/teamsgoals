from teamsgoals.player.Repository.player_repository import PlayerRepository
from teamsgoals.teams.Repository.teams_repository import TeamsRepository


class PlayersService:

    def __init__(self, json_response):
        self.json_response = json_response
        self.teams_repository = TeamsRepository()
        self.player_repository = PlayerRepository()

    def get_data_players(self, id_player=None):
        data_player = self.player_repository.get_info_player_by_id(id_player=id_player) if id_player else \
            self.player_repository.get_info_players_all()
        if data_player:
            self.get_json_response(data_player=data_player)
        else:
            self.json_response['incidents'].append('No data to display')
        return self.json_response

    def get_json_response(self, data_player):
        for player in data_player:
            self.json_response['result'].append({
                'player_id': player.id,
                'name': player.name,
                'goals': player.goals,
                'team': player.team.name
            })

    def add_player(self, request):
        # noinspection PyBroadException
        try:
            if request.data['name'] and int(request.data['goals']) and request.data['team_id']:
                self.player_repository.add_player(name=request.data['name'], goals=request.data['goals'],
                                                  team=request.data['team_id'])
                self.json_response['result'] = 'The record was entered correctly.'
            else:
                self.json_response['incidents'].append('Expected parameters were not provided.')
        except Exception:
            self.json_response['incidents'].append('An error occurred while inserting the record.')
        return self.json_response

    def update_player(self, request, id_player):
        # noinspection PyBroadException
        try:
            data_player = self.player_repository.get_info_player_by_id_object(id_player=id_player)
            if data_player:
                self.player_repository.update_player(request=request, player=data_player)
                self.json_response['result'] = 'The record has been successfully updated.'
            else:
                self.json_response['incidents'].append('The team to look for does not exist')
        except Exception:
            self.json_response['incidents'].append('An error occurred while updating the registry.')
        return self.json_response

    def delete_player(self, id_player):
        # noinspection PyBroadException
        try:
            data_player = self.player_repository.get_info_player_by_id_object(id_player=id_player)
            if data_player:
                self.player_repository.delete_player(player=data_player)
                self.json_response['result'] = 'The record has been deleted successfully.'
            else:
                self.json_response['incidents'].append('The team to look for does not exist')
        except Exception:
            self.json_response['incidents'].append('An error occurred while deleting the record.')
        return self.json_response
