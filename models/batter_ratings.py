class BatterRatings(object):

    def __init__(self):
        self.player_id = None
        self.contact = None
        self.gap = None
        self.power = None
        self.eye = None
        self.avoid_k = None
        self.contact_r = None
        self.gap_r = None
        self.power_r = None
        self.eye_r = None
        self.avoid_k_r = None
        self.contact_l = None
        self.gap_l = None
        self.power_l = None
        self.eye_l = None
        self.avoid_k_l = None
        self.pot_contact = None
        self.pot_gap = None
        self.pot_power = None
        self.pot_eye = None
        self.pot_avoid_k = None

    def save(self, cur, date_id):
        cur.execute('''
            insert into batting_ratings
            (player_id, date_id,
             contact, gap, power, eye, avoid_k,
             contact_r, gap_r, power_r, eye_r, avoid_k_r,
             contact_l, gap_l, power_l, eye_l, avoid_k_l,
             pot_contact, pot_gap, pot_power, pot_eye, pot_avoid_k)
            values
            (?, ?,
             ?, ?, ?, ?, ?,
             ?, ?, ?, ?, ?,
             ?, ?, ?, ?, ?,
             ?, ?, ?, ?, ?)''',
            (self.player_id, date_id,
             self.contact, self.gap, self.power, self.eye, self.avoid_k,
             self.contact_r, self.gap_r, self.power_r, self.eye_r, self.avoid_k_r,
             self.contact_l, self.gap_l, self.power_l, self.eye_l, self.avoid_k_l,
             self.pot_contact, self.pot_gap, self.pot_power, self.pot_eye, self.pot_avoid_k))

    def is_updated(self, ratings):
        return self.contact != ratings.contact or \
            self.gap != ratings.gap or \
            self.power != ratings.power or \
            self.eye != ratings.eye or \
            self.avoid_k != ratings.avoid_k or \
            self.contact_r != ratings.contact_r or \
            self.gap_r != ratings.gap_r or \
            self.power_r != ratings.power_r or \
            self.eye_r != ratings.eye_r or \
            self.avoid_k_r != ratings.avoid_k_r or \
            self.contact_l != ratings.contact_l or \
            self.gap_l != ratings.gap_l or \
            self.power_l != ratings.power_l or \
            self.eye_l != ratings.eye_l or \
            self.avoid_k_l != ratings.avoid_k_l or \
            self.pot_contact != ratings.pot_contact or \
            self.pot_gap != ratings.pot_gap or \
            self.pot_power != ratings.pot_power or \
            self.pot_eye != ratings.pot_eye or \
            self.pot_avoid_k != ratings.pot_avoid_k