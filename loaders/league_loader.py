import configuration

from bs4 import BeautifulSoup
from loaders.loader import Loader
from models.league import League

class LeagueLoader(Loader):

    def get_home_soup(self, league_id):
        return self.get_soup('{}/leagues/league_{}_home.html'.format(configuration.ROOT, league_id))

    def get_team_soup(self, league_id):
        return self.get_soup('{}/leagues/league_{}_teams.html'.format(configuration.ROOT, league_id))

    def get_index_soup(self):
        return self.get_soup('{}/index.html'.format(configuration.ROOT))

    def get_waiver_wire_soup(self, league_id):
        return self.get_soup('{}/leagues/league_{}_waiver_wire_block.html'.format(configuration.ROOT, league_id))

    def get_injury_soup(self, league_id):
        return self.get_soup('{}/leagues/league_{}_injuries_report.html'.format(configuration.ROOT, league_id))

    def get_finance_soup(self, league_id):
        return self.get_soup('{}/leagues/league_{}_financial_report.html'.format(configuration.ROOT, league_id))

    def load_league(self, league_id):
        home_soup = self.get_home_soup(league_id)
        team_soup = self.get_team_soup(league_id)
        league = League()
        league.id = league_id
        league.name = self.get_name(home_soup)
        league.is_major = self.get_is_major(home_soup)
        league.team_ids = self.get_team_ids(team_soup)
        league.parent_id = self.get_parent_id(home_soup)
        league.short_name = self.get_short_name(home_soup)
        if league.is_major:
            waiver_soup = self.get_waiver_wire_soup(league_id)
            injury_soup = self.get_injury_soup(league_id)
            finance_soup = self.get_finance_soup(league_id)
            league.waiver_wire = self.get_waiver_wire(waiver_soup)
            league.injured_player_ids = self.get_injured_player_ids(injury_soup)
            league.payrolls = self.get_payrolls(finance_soup)
        return league

    def load_all(self):
        leagues = []
        index_soup = self.get_index_soup()
        for league_id in self.get_league_ids(index_soup):
            leagues.append(self.load_league(league_id))
        return leagues

    def get_league_ids(self, soup):
        pass

    def get_name(self, soup):
        pass

    def get_is_major(self, soup):
        pass

    def get_team_ids(self, soup):
        pass

    def get_parent_id(self, soup):
        pass

    def get_short_name(self, soup):
        pass

    def get_waiver_wire(self, soup):
        pass

    def get_injured_player_ids(self, soup):
        pass

    def get_payrolls(self, soup):
        pass