import configuration

from cache import TEAM_CACHE
from loaders.loader import Loader
from models.team import Team

class TeamLoader(Loader):

    def get_team_roster_soup(self, team_id):
        return self.get_soup('{}/teams/team_{}_roster_page.html'.format(configuration.ROOT, team_id))

    def get_team_home_soup(self, team_id):
        return self.get_soup('{}/teams/team_{}.html'.format(configuration.ROOT, team_id))

    def load_team(self, team_id):
        if TEAM_CACHE.has_key(team_id):
            return TEAM_CACHE[team_id]
        roster_soup = self.get_team_roster_soup(team_id)
        home_soup = self.get_team_home_soup(team_id)
        team = Team()
        team.id = team_id
        team.name = self.get_name(roster_soup)
        team.level = self.get_level(roster_soup)
        team.parent_team_id = self.get_parent_team_id(home_soup)
        team.player_positions = self.get_player_positions(roster_soup)
        TEAM_CACHE[team_id] = team
        return team

    def get_name(self, soup):
        pass

    def get_level(self, soup):
        pass

    def get_parent_team_id(self, soup):
        pass

    def get_player_positions(self, soup):
        pass