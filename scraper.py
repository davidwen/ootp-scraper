import configuration
import os
import sqlite3

from contextlib import closing
from ootp15.league_loader import LeagueLoader
from ootp15.player_loader import PlayerLoader
from ootp15.team_loader import TeamLoader

class Scraper(object):

    def __init__(self):
        pass

    def save_stats(self):
        with closing(sqlite3.connect(configuration.DATABASE)) as db:
            cur = db.cursor()
            for dirname, dirnames, filenames in os.walk(configuration.ROOT + '/players'):
                for filename in filenames:
                    if filename[0] == '.':
                        continue
                    player_id = int(filename.split('_')[1].split('.')[0])
                    print player_id
                    try:
                        player = PlayerLoader(player_id).player
                        player.save_stats(cur)
                        db.commit()
                    except:
                        print 'ERROR ' + str(player_id)

if __name__ == '__main__':
    Scraper().save_stats()