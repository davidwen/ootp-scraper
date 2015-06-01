import re

from models.league import League
from loaders import league_loader

class LeagueLoader(league_loader.LeagueLoader):

    def get_league_ids(self, soup):
        league_ids = []
        links = soup.find_all('a', text=re.compile('League Home'))
        for link in links:
            url = link['href']
            league_ids.append(int(url.split('_')[1].split('.')[0]))
        return league_ids

    def get_name(self, soup):
        return soup.find('img')['title']

    def get_team_ids(self, soup):
        team_ids = []
        tables = soup.find_all('table')[-4:-1]
        for table in tables:
            links = table.find_all('a')
            for link in links:
                url = link['href']
                if 'teams/team' in url:
                    team_ids.append(int(url.split('_')[1].split('.')[0]))
        return team_ids