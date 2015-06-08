import re

from loaders import team_loader

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