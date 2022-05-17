from django.db.models import Sum

from teamsgoals.models import Player


class PlayerRepository:

    @staticmethod
    def get_sum_goals(id_team):
        return Player.objects.filter(team=id_team).aggregate(Sum('goals'))

    @staticmethod
    def get_info_player_by_id(id_player):
        return Player.objects.filter(id=id_player)

    @staticmethod
    def get_info_players_all():
        return Player.objects.all()

    @staticmethod
    def add_player(name, goals, team):
        player = Player(
            name=name,
            goals=goals,
            team_id=team
        )
        player.save()

    @staticmethod
    def get_info_player_by_id_object(id_player):
        return Player.objects.get(pk=id_player)

    @staticmethod
    def update_player(request, player):
        if request.data['name']:
            player.name = request.data['name']
        if request.data['goals']:
            player.goals = request.data['goals']
        player.save()

    @staticmethod
    def delete_player(player):
        player.delete()

