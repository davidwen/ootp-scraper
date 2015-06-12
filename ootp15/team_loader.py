import re

from loaders import team_loader
from ootp15.league_loader import LeagueLoader

class TeamLoader(team_loader.TeamLoader):

    def get_name(self):
        full_name = self.roster_soup.find_all('img')[3]['title']
        if '(' in full_name:
            return full_name[:full_name.find('(') - 1]
        else:
            return full_name

    def get_level(self):
        full_name = self.roster_soup.find_all('img')[3]['title']
        if '(' in full_name:
            return full_name[full_name.find('(') + 1:full_name.find(')')]
        else:
            return 'ML'

    def get_parent_team_id(self):
        link = self.home_soup.find(text=re.compile('LINKS')).parent.parent.parent.find_all('a')[-1]
        if 'minor' not in link['href']:
            return int(link['href'].split('_')[1].split('.')[0])
        else:
            return self.team_id

    def get_league_id(self):
        link = self.home_soup.find('a')
        return int(link['href'].split('_')[1].split('.')[0])

    def get_short_name(self):
        league_id = self.get_league_id()
        league = LeagueLoader().load_league(league_id)
        return league.team_short_names[self.team_id]

    def get_player_positions(self):
        player_positions = {}
        tables = self.roster_soup.find_all('table', class_='data sortable')
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                links = row.find_all('a')
                if not links:
                    continue
                player_link = links[0]
                team_link = links[1]
                team_url = team_link['href']
                team_id = int(team_url.split('_')[1].split('.')[0])
                if self.team_id == team_id:
                    player_url = player_link['href']
                    player_id = int(player_url.split('_')[1].split('.')[0])
                    position = row.find_all('td')[1].text
                    player_positions[player_id] = position
        return player_positions

    def get_disabled_list_player_ids(self):
        disabled_list_player_ids = set()
        dl = self.roster_soup.find('td', text=re.compile('DISABLED LIST'))
        if dl:
            table = dl.parent.next_sibling.next_sibling.find('table')
            rows = table.find_all('tr')
            for row in rows:
                link = row.find('a')
                if link:
                    player_id = int(link['href'].split('_')[1].split('.')[0])
                    disabled_list_player_ids.add(player_id)
        return disabled_list_player_ids