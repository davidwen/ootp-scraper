import configuration
import os
import sqlite3

from constants import PITCHING_POSITIONS
from contextlib import closing
from models.batter_ratings import BatterRatings
from models.pitcher_ratings import PitcherRatings
from ootp15.date_loader import DateLoader
from ootp15.player_loader import PlayerLoader

class RatingsScraper(object):

    def __init__(self):
        pass

    def save_ratings(self):
        with closing(sqlite3.connect(configuration.DATABASE)) as db:
            cur = db.cursor()
            date_id = self.get_date_id(cur)
            db.commit()
            for dirname, dirnames, filenames in os.walk(configuration.ROOT + '/players'):
                for filename in filenames:
                    if filename[0] == '.':
                        continue
                    player_id = int(filename.split('_')[1].split('.')[0])
                    print player_id
                    player = PlayerLoader(player_id).player
                    if not player.retired:
                        prev_ratings = self.get_prev_ratings(cur, player)
                        if prev_ratings is None or player.has_updated_ratings(prev_ratings):
                            player.save_ratings(cur, date_id)
                            db.commit()

    # def save_ratings(self):
    #     with closing(sqlite3.connect(configuration.DATABASE)) as db:
    #         cur = db.cursor()
    #         date_id = self.get_date_id(cur)
    #         cur.execute('select id from players where retired = 0 and id > 0')
    #         for row in cur.fetchall():
    #             player_id = int(row[0])
    #             print player_id
    #             player = PlayerLoader(player_id).player
    #             if not player.retired:
    #                 prev_ratings = self.get_prev_ratings(cur, player)
    #                 if prev_ratings is None or player.has_updated_ratings(prev_ratings):
    #                     player.save_ratings(cur, date_id)
    #                     db.commit()

    def get_date_id(self, cur):
        current_date = DateLoader().date
        cur.execute('''
            insert or ignore into dates
            (date)
            values
            (?)''', ([current_date]))
        cur.execute('select id from dates where date = ?', ([current_date]))
        return cur.fetchone()[0]

    def get_prev_ratings(self, cur, player):
        if player.position in PITCHING_POSITIONS:
            cur.execute('''
                select
                    last.stuff, last.movement, last.control,
                    last.stuff_l, last.movement_l, last.control_l,
                    last.stuff_r, last.movement_r, last.control_r,
                    last.pot_stuff, last.pot_movement, last.pot_control,
                    last.stamina, last.velocity, last.hold, last.groundball
                from pitching_ratings last
                left join pitching_ratings later
                    on later.player_id = last.player_id
                    and later.date_id > last.date_id
                where later.date_id is null
                and last.player_id = ?''', (player.id,))
            row = cur.fetchone()
            if row:
                pitcher_ratings = PitcherRatings()
                pitcher_ratings.player_id = player.id
                pitcher_ratings.stuff = row[0]
                pitcher_ratings.movement = row[1]
                pitcher_ratings.control = row[2]
                pitcher_ratings.stuff_l = row[3]
                pitcher_ratings.movement_l = row[4]
                pitcher_ratings.control_l = row[5]
                pitcher_ratings.stuff_r = row[6]
                pitcher_ratings.movement_r = row[7]
                pitcher_ratings.control_r = row[8]
                pitcher_ratings.pot_stuff = row[9]
                pitcher_ratings.pot_movement = row[10]
                pitcher_ratings.pot_control = row[11]
                pitcher_ratings.stamina = row[12]
                pitcher_ratings.velocity = row[13]
                pitcher_ratings.hold = row[14]
                pitcher_ratings.groundball = row[15]
                return pitcher_ratings
        else:
            cur.execute('''
                select
                    last.contact, last.gap, last.power, last.eye, last.avoid_k,
                    last.contact_r, last.gap_r, last.power_r, last.eye_r, last.avoid_k_r,
                    last.contact_l, last.gap_l, last.power_l, last.eye_l, last.avoid_k_l,
                    last.pot_contact, last.pot_gap, last.pot_power, last.pot_eye, last.pot_avoid_k
                from batting_ratings last
                left join batting_ratings later
                    on later.player_id = last.player_id
                    and later.date_id > last.date_id
                where later.date_id is null
                and last.player_id = ?''', (player.id,))
            row = cur.fetchone()
            if row:
                batter_ratings = BatterRatings()
                batter_ratings.player_id = player.id
                batter_ratings.contact = row[0]
                batter_ratings.gap = row[1]
                batter_ratings.power = row[2]
                batter_ratings.eye = row[3]
                batter_ratings.avoid_k = row[4]
                batter_ratings.contact_r = row[5]
                batter_ratings.gap_r = row[6]
                batter_ratings.power_r = row[7]
                batter_ratings.eye_r = row[8]
                batter_ratings.avoid_k_r = row[9]
                batter_ratings.contact_l = row[10]
                batter_ratings.gap_l = row[11]
                batter_ratings.power_l = row[12]
                batter_ratings.eye_l = row[13]
                batter_ratings.avoid_k_l = row[14]
                batter_ratings.pot_contact = row[15]
                batter_ratings.pot_gap = row[16]
                batter_ratings.pot_power = row[17]
                batter_ratings.pot_eye = row[18]
                batter_ratings.pot_avoid_k = row[19]
                return batter_ratings