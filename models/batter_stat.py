class BatterStat(object):

    def __init__(self):
        self.player_id = None
        self.position = None
        self.g = None
        self.ab = None
        self.h = None
        self.double = None
        self.triple = None
        self.hr = None
        self.rbi = None
        self.r = None
        self.bb = None
        self.hp = None
        self.sf = None
        self.k = None
        self.sb = None
        self.cs = None
        self.vorp = None
        self.war = None

    def get_pa(self):
        return self.ab + self.bb + self.hp + self.sf

    def get_avg(self):
        if self.ab:
            return round(float(self.h) / self.ab, 3)

    def get_obp(self):
        if self.get_pa():
            return round(float(self.h + self.bb + self.hp) / self.get_pa(), 3)

    def get_slg(self):
        if self.ab:
            total_bases = self.h + self.double + (2 * self.triple) + (3 * self.hr)
            return round(total_bases / float(self.ab), 3)

    def get_ops(self):
        if self.get_pa() and self.ab:
            return round(self.get_obp() + self.get_slg(), 3)

    def get_babip(self):
        balls_in_play = self.ab - self.k - self.hr + self.sf
        if balls_in_play > 0:
            return round(
                float(self.h - self.hr) / balls_in_play, 3)

    def get_krate(self):
        if self.get_pa():
            return round(float(self.k) / self.get_pa(), 2)

    def get_bbrate(self):
        if self.get_pa():
            return round(float(self.bb) / self.get_pa(), 2)

    def save(self, cur):
        pass