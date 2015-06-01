import configuration

from bs4 import BeautifulSoup
from cache import TEAM_CACHE
from models.team import Team

class TeamLoader(object):
    
    def __init__(self):
        pass

    def get_soup(self, team_id):
        filename = '{}/teams/team_{}_roster_page.html'.format(configuration.ROOT, team_id)
        with open(filename, 'rb') as f:
            return BeautifulSoup(f.read())

    def load_team(self, team_id):
        if TEAM_CACHE.has_key(team_id):
            return TEAM_CACHE[team_id]
        soup = self.get_soup(team_id)
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