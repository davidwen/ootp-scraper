from ootp15.check_scraper import CheckScraper
from ootp15.league_scraper import LeagueScraper
from ootp15.ratings_scraper import RatingsScraper
from ootp15.stats_scraper import StatsScraper
from ootp15.team_scraper import TeamScraper
from ootp15.waiver_wire_scraper import WaiverWireScraper

class OOTP15Scraper(object):

    def __init__(self):
        pass

    def scrape(self):
        StatsScraper().save_stats()
        CheckScraper().update_checks()
        WaiverWireScraper().update_waiver_wire()
        RatingsScraper().save_ratings()
        LeagueScraper().save_leagues()
        TeamScraper().save_teams()

if __name__ == '__main__':
    OOTP15Scraper().scrape()
