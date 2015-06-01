import configuration

from bs4 import BeautifulSoup
from loaders.loader import Loader

class FreeAgentsLoader(Loader):

    FREE_AGENTS_CACHE = None
    
    def __init__(self):
        if FreeAgentsLoader.FREE_AGENTS_CACHE:
            self.player_positions = FreeAgentsLoader.FREE_AGENTS_CACHE.player_positions
        else:
            self.batter_soup = self.get_free_agents_soup(0)
            self.pitcher_soup = self.get_free_agents_soup(1)
            self.player_positions = self.get_player_positions()
            FreeAgentsLoader.FREE_AGENTS_CACHE = self
        Loader.__init__(self)

    def get_free_agents_soup(self, tab):
        league_id = self.get_league_id()
        return self.get_soup('{}/leagues/league_{}_free_agents_report_{}.html'.format(configuration.ROOT, league_id, tab))

    def get_league_id(self):
        pass

    def get_player_positions(self):
        pass