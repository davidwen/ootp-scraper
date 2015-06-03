import re

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

    def get_is_major(self, soup):
        return soup.find('a', text=re.compile('Top Systems')) is not None

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

    def get_waiver_wire(self, soup):
        waiver_wire = {}
        tables = soup.find_all('table', class_='data sortable')
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                links = row.find_all('a')
                if links:
                    player_id = int(links[0]['href'].split('_')[1].split('.')[0])
                    team_id = int(links[1]['href'].split('_')[1].split('.')[0])
                    waiver_wire[player_id] = team_id
        return waiver_wire