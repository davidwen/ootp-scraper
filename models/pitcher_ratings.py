class PitcherRatings(object):

    def __init__(self):
        self.player_id = None
        self.stuff = None
        self.movement = None
        self.control = None
        self.stuff_l = None
        self.movement_l = None
        self.control_l = None
        self.stuff_r = None
        self.movement_r = None
        self.control_r = None
        self.pot_stuff = None
        self.pot_movement = None
        self.pot_control = None
        self.stamina = None
        self.velocity = None
        self.hold = None
        self.groundball = None

    def save(self, cur, date_id):
        cur.execute('''
            insert into pitching_ratings
            (player_id, date_id,
             stuff, movement, control,
             stuff_l, movement_l, control_l,
             stuff_r, movement_r, control_r,
             pot_stuff, pot_movement, pot_control,
             stamina, velocity, hold, groundball)
            values
            (?, ?,
             ?, ?, ?,
             ?, ?, ?,
             ?, ?, ?,
             ?, ?, ?,
             ?, ?, ?, ?)''',
            (self.player_id, date_id,
             self.stuff, self.movement, self.control,
             self.stuff_l, self.movement_l, self.control_l,
             self.stuff_r, self.movement_r, self.control_r,
             self.pot_stuff, self.pot_movement, self.pot_control,
             self.stamina, self.velocity, self.hold, self.groundball))