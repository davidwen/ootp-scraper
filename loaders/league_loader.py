import configuration

from bs4 import BeautifulSoup
from models.league import League

class LeagueLoader(object):
    
    def __init__(self):
        pass

    def get_soup(self, league_id):
        filename = '{}/leagues/league_{}_home.html'.format(configuration.ROOT, league_id)
        with open(filename, 'rb') as f:
            return BeautifulSoup(f.read())

    def get_index_soup(self):
        filename = '{}/index.html'.format(configuration.ROOT)
        with open(filename, 'rb') as f:
            return BeautifulSoup(f.read())        

    def load_league(self, league_id):
        soup = self.get_soup(league_id)
        league = League()
        league.id = league_id
        league.name = self.get_name(soup)
        league.team_ids = self.get_team_ids(soup)
        return league

    def load_all(self):
        leagues = []
        soup = self.get_index_soup()
        for league_id in self.get_league_ids(soup):
            leagues.append(self.load_league(league_id))
        return leagues

    def get_league_ids(self, soup):
        pass

    def get_name(self, soup):
        pass

    def get_team_ids(self, soup):
        pass