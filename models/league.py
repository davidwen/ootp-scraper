class League(object):

    def __init__(self):
        self.id = None
        self.name = None
        self.short_name = None
        self.is_major = None
        self.team_ids = None
        self.waiver_wire = None
        self.injured_player_ids = None
        self.payrolls = None
        self.team_short_names = None

    def save(self, cur):
        cur.execute('''
            insert or replace into leagues
            (id, name, short_name)
            values
            (?, ?, ?)''', (self.id, self.name, self.short_name))