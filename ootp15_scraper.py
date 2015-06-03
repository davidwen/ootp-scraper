from ootp15.ratings_scraper import RatingsScraper
from ootp15.stats_scraper import StatsScraper
from ootp15.waiver_wire_scraper import WaiverWireScraper

class OOTP15Scraper(object):

    def __init__(self):
        pass

    def scrape(self):
        # StatsScraper().save_stats()
        # WaiverWireScraper().update_waiver_wire()
        RatingsScraper().save_ratings()

if __name__ == '__main__':
    OOTP15Scraper().scrape()