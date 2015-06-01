from models import pitcher_stat

class PitcherSeasonStat(pitcher_stat.PitcherStat):

    def __init__(self):
        self.year = None
        self.team_id = None
        pitcher_stat.PitcherStat.__init__(self)

    def save(self, cur):
        cur.execute('''
            insert or replace into season_pitching_stats
            (year, player_id, team_id,
             g, gs, w, l, sv,
             outs, ha, r, er, hr, bb, k, cg, sho,
             vorp, war,
             era, whip, k9, bb9, kbb)
            values
            (?, ?, ?,
             ?, ?, ?, ?, ?,
             ?, ?, ?, ?, ?, ?, ?, ?, ?,
             ?, ?,
             ?, ?, ?, ?, ?)''',
            (self.year, self.player_id, self.team_id,
             self.g, self.gs, self.w, self.l, self.sv,
             self.outs, self.ha, self.r, self.er, self.hr, self.bb, self.k, self.cg, self.sho,
             self.vorp, self.war,
             self.get_era(), self.get_whip(), self.get_k9(), self.get_bb9(), self.get_kbb()))