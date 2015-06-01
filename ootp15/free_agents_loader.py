from loaders import free_agents_loader
from ootp15.league_loader import LeagueLoader

class FreeAgentsLoader(free_agents_loader.FreeAgentsLoader):

    def get_league_id(self):
        return LeagueLoader().load_all()[0].id

    def get_player_positions(self):
        player_positions = {}
        soups = [self.batter_soup, self.pitcher_soup]
        for soup in soups:
            table = soup.find('table', class_='data sortable')
            for row in table.find_all('tr')[1:]:
                link = row.find('a')
                player_id = int(link['href'].split('_')[1].split('.')[0])
                position = row.find_all('td')[3].text
                player_positions[player_id] = position
        return player_positions