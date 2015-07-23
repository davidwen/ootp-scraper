from bs4 import BeautifulSoup
import configuration
import os
import sqlite3

from contextlib import closing
from ootp15.date_loader import DateLoader
from ootp15.league_loader import LeagueLoader

class RetireScraper(object):

    def update_retired(self):
        with closing(sqlite3.connect(configuration.DATABASE)) as db:
            cur = db.cursor()
            date_id = self.get_date_id(cur)
            leagues = LeagueLoader().load_all()
            leagues = [league for league in leagues if league.is_major]
            for league in leagues:
                with open('{}/leagues/league_{}_all_transactions_0_0.html'.format(configuration.ROOT, league.id), 'rb') as f:
                    soup = BeautifulSoup(f.read())
                    retired = self.get_retired(soup)
                    for player_id in retired:
                        cur.execute('''
                            select retired from players where id = ?''', (player_id,))
                        if cur.fetchone()[0] == 0:
                            cur.execute('''
                                insert or ignore into player_teams
                                (player_id, date_id, team_id)
                                values
                                (?, ?, 0)''', (player_id, date_id))
                            cur.execute('''
                                update players set retired = 1 where id = ?''', (player_id,))
                            cur.execute('''
                                select count(*) from (
                                    select player_id
                                    from batting_stats
                                    where player_id = ?
                                    union all
                                    select player_id
                                    from pitching_stats
                                    where player_id = ?)''', (player_id, player_id))
                            if cur.fetchone()[0] == 0:
                                cur.execute('''
                                    delete from players where id = ?''', (player_id,))
            db.commit()

    def get_retired(self, soup):
        tds = soup.find_all('td')
        retired = []
        for td in tds:
            if 'retires' in td.text:
                links = td.find_all('a')
                if len(links) == 3:
                    retired.append(int(links[1]['href'].split('_')[1].split('.')[0]))
        return retired

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