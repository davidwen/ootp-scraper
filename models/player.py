from models.batter_career_stat import BatterCareerStat
from models.pitcher_career_stat import PitcherCareerStat

class Player(object):

    def __init__(self):
        self.id = None
        self.name = None
        self.birthday = None
        self.leadership = None
        self.loyalty = None
        self.desire_for_win = None
        self.greed = None
        self.intelligence = None
        self.work_ethic = None
        self.bats = None
        self.throws = None
        self.position = None
        self.pitching_stats = None
        self.batting_stats = None
        self.career_positions = None
        self.retired = None

    def save(self, cur):
        cur.execute('''
            insert or replace into players
            (id, name, birthday,
             leadership, loyalty, desire_for_win, greed, intelligence, work_ethic,
             bats, throws, position, retired)
            values
            (?, ?, ?,
             ?, ?, ?, ?, ?, ?,
             ?, ?, ?, ?)''',
            (self.id, self.name, self.birthday,
             self.leadership, self.loyalty, self.desire_for_win, self.greed, self.intelligence, self.work_ethic,
             self.bats, self.throws, self.position, self.retired))

    def save_stats(self, cur):    
        self.save(cur)
        if self.pitching_stats:
            for stat in self.pitching_stats:
                stat.save(cur)
            PitcherCareerStat().combine(self.pitching_stats).save(cur)
        if self.batting_stats:
            for stat in self.batting_stats:
                stat.save(cur)
            BatterCareerStat().combine(self.batting_stats).save(cur)

    def save_ratings(self, cur, date_id):
        self.save(cur)
        if self.pitching_ratings:
            self.pitching_ratings.save(cur, date_id)
        if self.batting_ratings:
            self.batting_ratings.save(cur, date_id)