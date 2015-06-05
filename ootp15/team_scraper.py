import configuration
import sqlite3

from contextlib import closing
from ootp15.date_loader import DateLoader
from ootp15.free_agents_loader import FreeAgentsLoader
from ootp15.league_loader import LeagueLoader
from ootp15.team_loader import TeamLoader

class TeamScraper(object):

    def save_teams(self):
        with closing(sqlite3.connect(configuration.DATABASE)) as db:
            cur = db.cursor()
            date_id = self.get_date_id(cur)
            old_player_teams = self.get_old_player_teams(cur)
            cur_player_teams = self.get_current_player_teams(cur)
            for player_id in cur_player_teams:
                if player_id not in old_player_teams or old_player_teams[player_id] != cur_player_teams[player_id]:
                    cur.execute('''
                        insert or ignore into player_teams
                        (player_id, date_id, team_id)
                        values
                        (?, ?, ?)''', (player_id, date_id, cur_player_teams[player_id]))
            db.commit()

    def get_old_player_teams(self, cur):
        old_player_teams = {}
        cur.execute('''
            select pt.player_id, pt.team_id
            from player_teams pt
            left join player_teams pt_later
              on pt_later.player_id = pt.player_id
              and pt_later.date_id > pt.date_id''')
        for row in cur.fetchall():
            old_player_teams[row[0]] = row[1]
        return old_player_teams

    def get_current_player_teams(self, cur):
        cur_player_teams = {}
        leagues = LeagueLoader().load_all()
        for league in leagues:
            for team_id in league.team_ids:
                team = TeamLoader(team_id).team
                cur.execute('''
                    insert or ignore into teams
                    (id, name, level, parent_id)
                    values
                    (?, ?, ?, ?)
                    ''', (team_id, team.name, team.level, team.parent_team_id))
                for player_id in team.player_positions:
                    cur_player_teams[player_id] = team_id
        for player_id in  FreeAgentsLoader().player_positions:
            cur_player_teams[player_id] = 0
        return cur_player_teams

    def get_date_id(self, cur):
        current_date = DateLoader().date
        cur.execute('''
            insert or ignore into dates
            (date)
            values
            (?)''', ([current_date]))
        cur.execute('select id from dates where date = ?', ([current_date]))
        return cur.fetchone()[0]