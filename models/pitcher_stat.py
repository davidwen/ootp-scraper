class PitcherStat(object):

    def __init__(self):
        self.player_id = None
        self.g = None
        self.gs = None
        self.w = None
        self.l = None
        self.sv = None
        self.outs = None
        self.ha = None
        self.r = None
        self.er = None
        self.hr = None
        self.bb = None
        self.k = None
        self.cg = None
        self.sho = None
        self.vorp = None
        self.war = None

    def get_ip(self):
        if self.outs:
            return self.outs / 3.0

    def get_era(self):
        if self.outs:
            return round(self.er * 9.0 / self.get_ip(), 2)

    def get_whip(self):
        if self.outs:
            return round((self.ha + self.bb) / self.get_ip(), 2)

    def get_k9(self):
        if self.outs:
            return round(self.k * 9.0 / self.get_ip(), 2)

    def get_bb9(self):
        if self.outs:
            return round(self.bb * 9.0 / self.get_ip(), 2)

    def get_kbb(self):
        if self.bb:
            return round(self.k * 1.0 / self.bb, 2)
        else:
            return None

    def save(self, cur):
        pass