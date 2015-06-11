import configuration
import sqlite3

from contextlib import closing
from ootp15.league_loader import LeagueLoader

class LeagueScraper(object):

    def save_leagues(self):
        with closing(sqlite3.connect(configuration.DATABASE)) as db:
            cur = db.cursor()
            leagues = LeagueLoader().load_all()
            for league in leagues:
                league.save(cur)
            db.commit()