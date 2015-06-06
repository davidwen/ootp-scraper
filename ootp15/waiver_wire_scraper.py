import configuration
import os
import sqlite3

from contextlib import closing
from ootp15.date_loader import DateLoader
from ootp15.league_loader import LeagueLoader

class WaiverWireScraper(object):

    def __init__(self):
        pass

    def update_waiver_wire(self):
        with closing(sqlite3.connect(configuration.DATABASE)) as db:
            cur = db.cursor()
            date_id = self.get_date_id(cur)
            leagues = LeagueLoader().load_all()
            for league in leagues:
                if league.waiver_wire:
                    for player_id in league.waiver_wire:
                        cur.execute('''
                            insert into waiver_wire
                            (date_id, player_id)
                            values
                            (?, ?)''' , (date_id, player_id))
            db.commit()

    def get_date_id(self, cur):
        current_date = DateLoader().date
        cur.execute('''
            insert or ignore into dates
            (date)
            values
            (?)''', ([current_date]))
        cur.execute('select id from dates where date = ?', ([current_date]))
        return cur.fetchone()[0]
