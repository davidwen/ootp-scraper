import configuration
import os
import sqlite3

from contextlib import closing
from ootp15.date_loader import DateLoader
from ootp15.league_loader import LeagueLoader
from ootp15.team_loader import TeamLoader

class CheckScraper(object):

    def __init__(self):
        pass

    def update_checks(self):
        with closing(sqlite3.connect(configuration.DATABASE)) as db:
            cur = db.cursor()
            date_id = self.get_date_id(cur)
            leagues = LeagueLoader().load_all()
            injured_player_ids = set()
            dl_player_ids = set()
            for league in leagues:
                if league.is_major:
                    if league.injured_player_ids:
                        for player_id in league.injured_player_ids:
                            injured_player_ids.add(player_id)
                    if league.payrolls:
                        for team_id in league.payrolls:
                            cur.execute('''
                                insert or ignore into payrolls
                                (date_id, team_id, payroll)
                                values
                                (?, ?, ?)''' , (date_id, team_id, league.payrolls[team_id]))
                    for team_id in league.team_ids:
                        team = TeamLoader(team_id).team
                        for player_id in team.disabled_list_player_ids:
                            dl_player_ids.add(player_id)
            for injured_player_id in injured_player_ids:
                if injured_player_id in dl_player_ids:
                    dl_player_ids.remove(injured_player_id)
            for dl_player_id in dl_player_ids:
                cur.execute('''
                    insert or ignore into healed_players
                    (date_id, player_id)
                    values
                    (?, ?)''', (date_id, dl_player_id))
            db.commit()

    def get_date_id(self, cur):
        current_date = DateLoader().date
        cur.execute('select id from dates where date = ?', (current_date,))
        row = cur.fetchone()
        if row:
            return row[0]
        cur.execute('select max(id) from dates')
        date_id = cur.fetchone()[0] + 1
        cur.execute('''
            insert into dates
            (id, date)
            values
            (?, ?)''', (date_id, current_date))
        return date_id