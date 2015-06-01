from collections import Counter
from models import batter_stat

class BatterCareerStat(batter_stat.BatterStat):

    def __init__(self):
        self.start_year = None
        self.end_year = None
        batter_stat.BatterStat.__init__(self)

    def combine(self, batting_stats):
        self.start_year = 9999
        positions = []
        self.g = 0
        self.ab = 0
        self.h = 0
        self.double = 0
        self.triple = 0
        self.hr = 0
        self.rbi = 0
        self.r = 0
        self.bb = 0
        self.hp = 0
        self.sf = 0
        self.k = 0
        self.sb = 0
        self.cs = 0
        self.vorp = 0
        self.war = 0
        for stat in batting_stats:
            self.player_id = stat.player_id
            positions.append(stat.position)
            self.start_year = min(self.start_year, stat.year)
            self.end_year = max(self.end_year, stat.year)
            self.g += stat.g
            self.ab += stat.ab
            self.h += stat.h
            self.double += stat.double
            self.triple += stat.triple
            self.hr += stat.hr
            self.rbi += stat.rbi
            self.r += stat.r
            self.bb += stat.bb
            self.hp += stat.hp
            self.sf += stat.sf
            self.k += stat.k
            self.sb += stat.sb
            self.cs += stat.cs
            self.vorp += stat.vorp
            self.war += stat.war
        most_common_position = Counter(positions).most_common(1)
        if len(most_common_position):
            self.position = most_common_position[0][0]
        return self

    def save(self, cur):
        cur.execute('''
            insert or replace into batting_stats
            (player_id, position, start_year, end_year,
             g, ab, h, double, triple, hr,
             rbi, r, bb, hp, sf, k, sb, cs,
             vorp, war,
             avg, obp, slg, ops, babip, krate, bbrate)
            values
            (?, ?, ?, ?,
             ?, ?, ?, ?, ?, ?,
             ?, ?, ?, ?, ?, ?, ?, ?,
             ?, ?,
             ?, ?, ?, ?, ?, ?, ?)''',
            (self.player_id, self.position, self.start_year, self.end_year,
             self.g, self.ab, self.h, self.double, self.triple, self.hr,
             self.rbi, self.r, self.bb, self.hp, self.sf, self.k, self.sb, self.cs,
             self.vorp, self.war,
             self.get_avg(), self.get_obp(), self.get_slg(), self.get_ops(), self.get_babip(), self.get_krate(), self.get_bbrate()))