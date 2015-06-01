import configuration
import re

from bs4 import BeautifulSoup
from cache import PLAYER_CACHE
from constants import PITCHING_POSITIONS
from models.player import Player

class PlayerLoader(object):
    
    def __init__(self, player_id):
        self.player_id = player_id
        self.soup = self.get_soup()
        self.player = self.load_player()

    def get_soup(self):
        filename = '{}/players/player_{}.html'.format(configuration.ROOT, self.player_id)
        with open(filename, 'rb') as f:
            return BeautifulSoup(f.read())

    def load_player(self):
        if PLAYER_CACHE.has_key(self.player_id):
            return PLAYER_CACHE[self.player_id]
        player = Player()
        player.id = self.player_id
        player.name = self.get_name()
        player.birthday = self.get_birthday()
        player.leadership = self.get_leadership()
        player.loyalty = self.get_loyalty()
        player.desire_for_win = self.get_desire_for_win()
        player.greed = self.get_greed()
        player.intelligence = self.get_intelligence()
        player.work_ethic = self.get_work_ethic()
        player.bats = self.get_bats()
        player.throws = self.get_throws()
        player.position = self.get_position()
        player.career_positions = self.get_career_positions()
        if player.position in PITCHING_POSITIONS:
            player.pitching_stats = self.get_pitching_stats(player)
        else:
            player.batting_stats = self.get_batting_stats(player)
        player.retired = self.get_retired()
        PLAYER_CACHE[self.player_id] = player
        return player

    def get_name(self):
        pass

    def get_birthday(self):
        pass

    def get_leadership(self):
        pass

    def get_loyalty(self):
        pass

    def get_desire_for_win(self):
        pass

    def get_greed(self):
        pass

    def get_intelligence(self):
        pass

    def get_work_ethic(self):
        pass

    def get_bats(self):
        pass

    def get_throws(self):
        pass

    def get_position(self):
        pass

    def get_career_positions(self):
        pass

    def get_batting_stats(self, player):
        pass

    def get_pitching_stats(self, player):
        pass

    def get_retired(self):
        pass

    def get_table_value(self, soup, key):
        return soup.find(text=re.compile(key)).parent.next_sibling.text