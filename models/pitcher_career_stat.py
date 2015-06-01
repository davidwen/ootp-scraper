from models import pitcher_stat

class PitcherCareerStat(pitcher_stat.PitcherStat):

    def __init__(self):
        self.start_year = None
        self.end_year = None
        pitcher_stat.PitcherStat.__init__(self)

    def combine(self, pitching_stats):
        self.start_year = 9999
        self.g = 0
        self.gs = 0
        self.w = 0
        self.l = 0
        self.sv = 0
        self.outs = 0
        self.ha = 0
        self.r = 0
        self.er = 0
        self.hr = 0
        self.bb = 0
        self.k = 0
        self.cg = 0
        self.sho = 0
        self.vorp = 0
        self.war = 0
        for stat in pitching_stats:
            self.player_id = stat.player_id
            self.start_year = min(self.start_year, stat.year)
            self.end_year = max(self.end_year, stat.year)
            self.g += stat.g
            self.gs += stat.gs
            self.w += stat.w
            self.l += stat.l
            self.sv += stat.sv
            self.outs += stat.outs
            self.ha += stat.ha
            self.r += stat.r
            self.er += stat.er
            self.hr += stat.hr
            self.bb += stat.bb
            self.k += stat.k
            self.cg += stat.cg
            self.sho += stat.sho
            self.vorp += stat.vorp
            self.war += stat.war
        return self

    def save(self, cur):
        cur.execute('''
            insert or replace into pitching_stats
            (player_id, start_year, end_year,
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
            (self.player_id, self.start_year, self.end_year,
             self.g, self.gs, self.w, self.l, self.sv,
             self.outs, self.ha, self.r, self.er, self.hr, self.bb, self.k, self.cg, self.sho,
             self.vorp, self.war,
             self.get_era(), self.get_whip(), self.get_k9(), self.get_bb9(), self.get_kbb()))