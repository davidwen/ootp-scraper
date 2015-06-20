from bs4 import BeautifulSoup
import configuration
import os
import re
import sqlite3
import urllib2

from contextlib import closing
from ootp15.date_loader import DateLoader
from ootp15.league_loader import LeagueLoader

class LeagueHistoryScraper(object):

    def __init__(self):
        pass

    def save_league_history(self):
        with closing(sqlite3.connect(configuration.DATABASE)) as db:
            cur = db.cursor()
            leagues = LeagueLoader().load_all()
            years = self.get_years(cur)
            for league in leagues:
                if league.is_major:
                    for year in years:
                        for division in range(0, 2):
                            print '{} {} {}'.format(league.id, year, division)
                            try:
                                response = urllib2.urlopen('http://worldbaseballhierarchy.com/lgreports/news/html/history/sl_stats_%d_%d_%d.html' % (league.id, division, year))
                                soup = BeautifulSoup(response.read())
                                self.update_league_history(cur, soup, league, year, division)
                            except urllib2.HTTPError:
                                pass
            db.commit()

    def get_years(self, cur):
        years = []
        cur.execute('select year from season_batting_stats group by year order by year')
        for row in cur.fetchall():
            years.append(row[0])
        return years

    def update_league_history(self, cur, soup, league, year, division):
        th = soup.find('th', text=re.compile('LEAGUE STANDINGS'))
        table = th.parent.parent.next_sibling.next_sibling
        rows = table.find_all('tr')
        for row in rows:
            if not row.find('a'):
                continue
            team_id = int(row.find('a')['href'].split('_')[2])
            tds = row.find_all('td')
            wins = tds[1].text
            losses = tds[2].text
            cur.execute('''
                insert or replace into team_leagues
                (team_id, year, league_id, division, wins, losses)
                values
                (?, ?, ?, ?, ?, ?)''', (team_id, year, league.id, 'LAD' if division == 0 else 'LOD', wins, losses))
