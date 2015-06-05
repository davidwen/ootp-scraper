import re

from constants import PERSONALITY_RATINGS
from loaders import player_loader
from team_loader import TeamLoader

from ootp15.batter_ratings_loader import BatterRatingsLoader
from ootp15.batter_stat_loader import BatterStatLoader
from ootp15.free_agents_loader import FreeAgentsLoader
from ootp15.pitcher_ratings_loader import PitcherRatingsLoader
from ootp15.pitcher_stat_loader import PitcherStatLoader

class PlayerLoader(player_loader.PlayerLoader):

    def get_name(self):
        return self.soup.find('img')['title']

    def get_birthday(self):
        return self.get_table_value(self.soup, 'Birthday:')

    def get_leadership(self):
        return PERSONALITY_RATINGS[self.get_table_value(self.soup, 'Leader Ability:')]

    def get_loyalty(self):
        return PERSONALITY_RATINGS[self.get_table_value(self.soup, 'Loyalty:')]

    def get_desire_for_win(self):
        return PERSONALITY_RATINGS[self.get_table_value(self.soup, 'Desire f. Win:')]

    def get_greed(self):
        return PERSONALITY_RATINGS[self.get_table_value(self.soup, 'Greed:')]

    def get_intelligence(self):
        return PERSONALITY_RATINGS[self.get_table_value(self.soup, 'Intelligence:')]

    def get_work_ethic(self):
        return PERSONALITY_RATINGS[self.get_table_value(self.soup, 'Work Ethic:')]

    def get_bats(self):
        data = self.get_bats_throws_data()
        return data[data.find('Bats:') + 6]

    def get_throws(self):
        data = self.get_bats_throws_data()
        return data[data.find('Throws:') + 8]

    def get_position(self):
        data = self.soup.find('div', class_='reptitle').text
        position = data.split(' ')[0]
        if position == 'P':
            team_id = self.get_team_id()
            if team_id:
                team = TeamLoader(self.get_team_id()).team
                if team.player_positions.has_key(self.player_id):
                    return team.player_positions[self.player_id]
            else:
                fa_loader = FreeAgentsLoader()
                if fa_loader.player_positions.has_key(self.player_id):
                    return fa_loader.player_positions[self.player_id]
        return position

    def get_career_positions(self):
        fielding_header = self.soup.find('th', text=re.compile('CAREER FIELDING STATS'))
        fielding_table = fielding_header.parent.parent.next_sibling.next_sibling
        rows = fielding_table.find_all('tr')
        best = {}
        for row in rows:
            link = row.find('a')
            if not link:
                continue
            url = link['href']
            split = url.split('_')
            year = int(split[3].split('.')[0])
            team_id = int(split[2])
            values = [td.string for td in row.find_all('td')]
            games = int(values[2])
            position = values[1]
            key = (year, team_id)
            if best.has_key(key):
                if games > best[key][1]:
                    best[key] = (position, games)
            else:
                best[key] = (position, games)
        career_positions = {}
        for key in best:
            career_positions[key] = best[key][0]
        return career_positions

    def get_batting_stats(self, player):
        return BatterStatLoader(self.soup, player).stats

    def get_pitching_stats(self, player):
        return PitcherStatLoader(self.soup, player).stats

    def get_batting_ratings(self, player):
        return BatterRatingsLoader(self.soup, player).ratings

    def get_pitching_ratings(self, player):
        return PitcherRatingsLoader(self.soup, player).ratings

    def get_retired(self):
        return self.get_table_value(self.soup, 'Contract:') == 'RETIRED'

    def get_bats_throws_data(self):
        return self.soup.find('div', text=re.compile('Age:*')).text

    def get_team_id(self):
        team_link = self.soup.find('a')['href']
        team_id = team_link.split('_')[1].split('.')[0]
        if team_id:
            return int(team_id)