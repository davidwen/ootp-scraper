import re

from models import batter_season_stat

class BatterStatLoader():

    def __init__(self, soup, player):
        self.soup = soup
        self.player = player
        self.stats = self.load_stats()

    def load_stats(self):
        stats = []
        for row in self.get_rows():
            link = row.find('a')
            if not link:
                continue

            history_url = row.find('a')['href']
            if history_url.find('team_year') == -1:
                continue

            stat_columns = row.find_all('td')
            stats.append(self.load_stat(history_url, stat_columns))
        return stats

    def load_stat(self, history_url, stat_columns):
        stat = batter_season_stat.BatterSeasonStat()
        stat.player_id = self.player.id
        stat.year = self.get_year(history_url)
        stat.team_id = self.get_team_id(history_url)
        stat.position = self.get_position(stat.year, stat.team_id)
        stat.g = self.get_g(stat_columns)
        stat.ab = self.get_ab(stat_columns)
        stat.h = self.get_h(stat_columns)
        stat.double = self.get_double(stat_columns)
        stat.triple = self.get_triple(stat_columns)
        stat.hr = self.get_hr(stat_columns)
        stat.rbi = self.get_rbi(stat_columns)
        stat.r = self.get_r(stat_columns)
        stat.bb = self.get_bb(stat_columns)
        stat.hp = self.get_hp(stat_columns)
        stat.sf = self.get_sf(stat_columns)
        stat.k = self.get_k(stat_columns)
        stat.sb = self.get_sb(stat_columns)
        stat.cs = self.get_cs(stat_columns)
        stat.vorp = self.get_vorp(stat_columns)
        stat.war = self.get_war(stat_columns)
        return stat

    def get_rows(self):
        career_batting_stats_table = self.soup.find('th', text=re.compile('Career Batting Stats')).parent.parent.next_sibling.next_sibling
        return career_batting_stats_table.find_all('tr')[1:]

    def get_year(self, history_url):
        return int(history_url.split('_')[3][0:4])

    def get_team_id(self, history_url):
        return int(history_url.split('_')[2])

    def get_position(self, year, team_id):
        if self.player.career_positions.has_key((year, team_id)):
            return self.player.career_positions[(year, team_id)]
        else:
            return self.player.position

    def get_g(self, stat_columns):
        return int(stat_columns[2].text)

    def get_ab(self, stat_columns):
        return int(stat_columns[3].text)

    def get_h(self, stat_columns):
        return int(stat_columns[4].text)

    def get_double(self, stat_columns):
        return int(stat_columns[5].text)

    def get_triple(self, stat_columns):
        return int(stat_columns[6].text)

    def get_hr(self, stat_columns):
        return int(stat_columns[7].text)

    def get_rbi(self, stat_columns):
        return int(stat_columns[8].text)

    def get_r(self, stat_columns):
        return int(stat_columns[9].text)

    def get_bb(self, stat_columns):
        return int(stat_columns[10].text)

    def get_hp(self, stat_columns):
        return int(stat_columns[11].text)

    def get_sf(self, stat_columns):
        return int(stat_columns[12].text)

    def get_k(self, stat_columns):
        return int(stat_columns[13].text)

    def get_sb(self, stat_columns):
        return int(stat_columns[14].text)

    def get_cs(self, stat_columns):
        return int(stat_columns[15].text)

    def get_vorp(self, stat_columns):
        return float(stat_columns[21].text)

    def get_war(self, stat_columns):
        return float(stat_columns[22].text)
