import configuration
import re

from loaders import date_loader
from ootp15.league_loader import LeagueLoader

class DateLoader(date_loader.DateLoader):

    def get_current_date(self):
        league_id = LeagueLoader().load_all()[0].id
        league_soup = self.get_soup('{}/leagues/league_{}_home.html'.format(configuration.ROOT, league_id))
        return league_soup.find('div', text=re.compile('HOME')).next_sibling.next_sibling.text