from loaders import team_loader

class TeamLoader(team_loader.TeamLoader):

    def get_name(self, soup):
        full_name = soup.find_all('img')[3]['title']
        if '(' in full_name:
            return full_name[:full_name.find('(') - 1]
        else:
            return full_name

    def get_level(self, soup):
        full_name = soup.find_all('img')[3]['title']
        if '(' in full_name:
            return full_name[full_name.find('(') + 1:full_name.find(')')]
        else:
            return 'ML'

    def get_player_positions(self, soup):
        player_positions = {}
        tables = soup.find_all('table', class_='data sortable')
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                link = row.find('a')
                if not link:
                    continue
                url = link['href']
                player_id = int(url.split('_')[1].split('.')[0])
                position = row.find_all('td')[1].text
                player_positions[player_id] = position
        return player_positions