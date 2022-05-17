from teamsgoals.player.Service.players_service import PlayersService


class PlayersController:

    def __init__(self, json_response):
        self.json_response = json_response

    def get_all_data_players(self):
        try:
            player_service = PlayersService(json_response=self.json_response)
            self.json_response = player_service.get_data_players()
        except Exception as error_logic:
            self.json_response['incidents'].append(error_logic)
        return self.json_response

    def add_player(self, request):
        try:
            player_service = PlayersService(json_response=self.json_response)
            self.json_response = player_service.add_player(request=request)
        except Exception as error_logic:
            self.json_response['incidents'].append(error_logic)
        return self.json_response

    def get_data_player_by_id(self, id_player):
        try:
            player_service = PlayersService(json_response=self.json_response)
            self.json_response = player_service.get_data_players(id_player=id_player)
        except Exception as error_logic:
            self.json_response['incidents'].append(error_logic)
        return self.json_response

    def update_data_player(self, id_player, request):
        try:
            player_service = PlayersService(json_response=self.json_response)
            self.json_response = player_service.update_player(request=request, id_player=id_player)
        except Exception as error_logic:
            self.json_response['incidents'].append(error_logic)
        return self.json_response

    def delete_player(self, id_player):
        try:
            player_service = PlayersService(json_response=self.json_response)
            self.json_response = player_service.delete_player(id_player=id_player)
        except Exception as error_logic:
            self.json_response['incidents'].append(error_logic)
        return self.json_response

