import configuration

from bs4 import BeautifulSoup

class FreeAgentsLoader(object):

    FREE_AGENTS_CACHE = None
    
    def __init__(self):
        if FreeAgentsLoader.FREE_AGENTS_CACHE:
            self.player_positions = FreeAgentsLoader.FREE_AGENTS_CACHE.player_positions
        else:
            self.batter_soup = self.get_soup(0)
            self.pitcher_soup = self.get_soup(1)
            self.player_positions = self.get_player_positions()
            FreeAgentsLoader.FREE_AGENTS_CACHE = self

    def get_soup(self, tab):
        league_id = self.get_league_id()
        filename = '{}/leagues/league_{}_free_agents_report_{}.html'.format(configuration.ROOT, league_id, tab)
        with open(filename, 'rb') as f:
            return BeautifulSoup(f.read())

    def get_league_id(self):
        pass

    def get_player_positions(self):
        pass