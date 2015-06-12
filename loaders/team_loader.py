import configuration

from cache import TEAM_CACHE
from loaders.loader import Loader
from models.team import Team

class TeamLoader(Loader):

    def __init__(self, team_id):
        self.team_id = team_id
        self.roster_soup = self.get_team_roster_soup()
        self.home_soup = self.get_team_home_soup()
        self.team = self.load_team()
        Loader.__init__(self)

    def get_team_roster_soup(self):
        return self.get_soup('{}/teams/team_{}_roster_page.html'.format(configuration.ROOT, self.team_id))

    def get_team_home_soup(self):
        return self.get_soup('{}/teams/team_{}.html'.format(configuration.ROOT, self.team_id))

    def load_team(self):
        if TEAM_CACHE.has_key(self.team_id):
            return TEAM_CACHE[self.team_id]
        roster_soup = self.get_team_roster_soup()
        home_soup = self.get_team_home_soup()
        team = Team()
        team.id = self.team_id
        team.name = self.get_name()
        team.short_name = self.get_short_name()
        team.level = self.get_level()
        team.parent_team_id = self.get_parent_team_id()
        team.league_id = self.get_league_id()
        team.player_positions = self.get_player_positions()
        team.disabled_list_player_ids = self.get_disabled_list_player_ids()
        TEAM_CACHE[self.team_id] = team
        return team

    def get_name(self):
        pass

    def get_short_name(self):
        pass

    def get_level(self):
        pass

    def get_parent_team_id(self):
        pass

    def get_league_id(self):
        pass

    def get_player_positions(self):
        pass

    def get_disabled_list_player_ids(self):
        pass