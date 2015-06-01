from models import batter_stat

class BatterSeasonStat(batter_stat.BatterStat):

    def __init__(self):
        self.year = None
        self.player_id = None
        batter_stat.BatterStat.__init__(self)

    def save(self, cur):
        cur.execute('''
            insert or replace into season_batting_stats
            (year, player_id, team_id, position,
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
            (self.year, self.player_id, self.team_id, self.position,
             self.g, self.ab, self.h, self.double, self.triple, self.hr,
             self.rbi, self.r, self.bb, self.hp, self.sf, self.k, self.sb, self.cs,
             self.vorp, self.war,
             self.get_avg(), self.get_obp(), self.get_slg(), self.get_ops(), self.get_babip(), self.get_krate(), self.get_bbrate()))