from ootp15.stats_scraper import StatsScraper
from ootp15.waiver_wire_scraper import WaiverWireScraper

class OOTP15Scraper(object):

    def __init__(self):
        pass

    def scrape(self):
        # StatsScraper().save_stats()
        WaiverWireScraper().update_waiver_wire()

if __name__ == '__main__':
    OOTP15Scraper().scrape()