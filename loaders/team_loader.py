import configuration

from cache import TEAM_CACHE
from loaders.loader import Loader
from models.team import Team

class TeamLoader(Loader):

    def get_team_soup(self, team_id):
        return self.get_soup('{}/teams/team_{}_roster_page.html'.format(configuration.ROOT, team_id))

    def load_team(self, team_id):
        if TEAM_CACHE.has_key(team_id):
            return TEAM_CACHE[team_id]
        soup = self.get_team_soup(team_id)
        team = Team()
        team.id = team_id
        team.name = self.get_name(soup)
        team.level = self.get_level(soup)
        team.player_positions = self.get_player_positions(soup)
        TEAM_CACHE[team_id] = team
        return team

    def get_name(self, soup):
        pass

    def get_level(self, soup):
        pass

    def get_player_positions(self, soup):
        pass