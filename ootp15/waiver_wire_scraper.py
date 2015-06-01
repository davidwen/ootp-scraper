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
            cur.execute('delete from current_date')

            current_date = DateLoader().get_current_date()
            cur.execute('insert into current_date (date) values (?)', ([current_date]))
            leagues = LeagueLoader().load_all()
            for league in leagues:
                if league.waiver_wire:
                    for player_id in league.waiver_wire:
                        cur.execute('''
                            insert into waiver_wire
                            (date, player_id)
                            values
                            (?, ?)''' , (current_date, player_id))
            db.commit()
