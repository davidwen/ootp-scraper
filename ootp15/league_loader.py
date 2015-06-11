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

    def get_short_name(self, soup):
        td = soup.find('td', class_='menu')
        return td.find_all('a')[1].text

    def get_team_ids(self, soup):
        team_ids = []
        links = soup.find_all('a', text=re.compile('Home Page'))
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

    def get_injured_player_ids(self, soup):
        injured_player_ids = set()
        links = soup.find_all('a')
        for link in links:
            if '/players/' in link['href']:
                injured_player_ids.add(int(link['href'].split('_')[1].split('.')[0]))
        return injured_player_ids

    def get_payrolls(self, soup):
        payrolls = {}
        table = soup.find('th', text=re.compile('Payroll')).parent.parent.parent
        rows = table.find_all('tr')
        for row in rows:
            link = row.find('a')
            if link:
                team_id = int(link['href'].split('_')[1].split('.')[0])
                payroll = int(re.sub('\D', '', row.find_all('td')[2].text))
                payrolls[team_id] = payroll
        return payrolls