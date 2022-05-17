from teamsgoals.models import Teams


class TeamsRepository:

    @staticmethod
    def get_info_teams_all():
        return Teams.objects.all()

    @staticmethod
    def get_info_team_by_id(id_team):
        return Teams.objects.filter(id=id_team)

    @staticmethod
    def get_info_team_by_id_object(id_team):
        return Teams.objects.get(pk=id_team)

    @staticmethod
    def add_team(name, city):
        team = Teams(
            name=name,
            city=city,
        )
        team.save()

    @staticmethod
    def update_team(request, team):
        if request.data['name']:
            team.name = request.data['name']
        if request.data['city']:
            team.city = request.data['city']
        team.save()

    @staticmethod
    def delete_team(team):
        team.delete()


