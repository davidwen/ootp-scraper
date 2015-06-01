import re

from models import pitcher_season_stat

class PitcherStatLoader():

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
        stat = pitcher_season_stat.PitcherSeasonStat()
        stat.player_id = self.player.id
        stat.year = self.get_year(history_url)
        stat.team_id = self.get_team_id(history_url)
        stat.g = self.get_g(stat_columns)
        stat.gs = self.get_gs(stat_columns)
        stat.w = self.get_w(stat_columns)
        stat.l = self.get_l(stat_columns)
        stat.sv = self.get_sv(stat_columns)
        stat.outs = self.get_outs(stat_columns)
        stat.ha = self.get_ha(stat_columns)
        stat.r = self.get_r(stat_columns)
        stat.er = self.get_er(stat_columns)
        stat.hr = self.get_hr(stat_columns)
        stat.bb = self.get_bb(stat_columns)
        stat.k = self.get_k(stat_columns)
        stat.cg = self.get_cg(stat_columns)
        stat.sho = self.get_sho(stat_columns)
        stat.vorp = self.get_vorp(stat_columns)
        stat.war = self.get_war(stat_columns)
        return stat

    def get_rows(self):
        career_pitching_stats_table = self.soup.find('th', text=re.compile('Career Pitching Stats')).parent.parent.next_sibling.next_sibling
        return career_pitching_stats_table.find_all('tr')[1:]

    def get_year(self, history_url):
        return int(history_url.split('_')[3][0:4])

    def get_team_id(self, history_url):
        return int(history_url.split('_')[2])

    def get_g(self, stat_columns):
        return int(stat_columns[2].text)

    def get_gs(self, stat_columns):
        return int(stat_columns[3].text)

    def get_w(self, stat_columns):
        return int(stat_columns[4].text)

    def get_l(self, stat_columns):
        return int(stat_columns[5].text)

    def get_sv(self, stat_columns):
        return int(stat_columns[6].text)

    def get_outs(self, stat_columns):
        ip = float(stat_columns[8].text)
        int_ip = int(ip)
        remainder_outs = (ip * 10) % 10
        return (3 * int_ip) + remainder_outs

    def get_ha(self, stat_columns):
        return int(stat_columns[9].text)

    def get_r(self, stat_columns):
        return int(stat_columns[10].text)

    def get_er(self, stat_columns):
        return int(stat_columns[11].text)

    def get_hr(self, stat_columns):
        return int(stat_columns[12].text)

    def get_bb(self, stat_columns):
        return int(stat_columns[13].text)

    def get_k(self, stat_columns):
        return int(stat_columns[14].text)

    def get_cg(self, stat_columns):
        return int(stat_columns[15].text)

    def get_sho(self, stat_columns):
        return int(stat_columns[16].text)

    def get_vorp(self, stat_columns):
        return float(stat_columns[19].text)

    def get_war(self, stat_columns):
        return float(stat_columns[20].text)
