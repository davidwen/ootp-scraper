import configuration
import re

from cache import PLAYER_CACHE
from constants import PITCHING_POSITIONS
from loaders.loader import Loader
from models.player import Player

class PlayerLoader(Loader):
    
    def __init__(self, player_id):
        self.player_id = player_id
        self.soup = self.get_player_soup()
        self.player = self.load_player()
        Loader.__init__(self)

    def get_player_soup(self):
        return self.get_soup('{}/players/player_{}.html'.format(configuration.ROOT, self.player_id))

    def load_player(self):
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
            player.pitching_ratings = self.get_pitching_ratings(player)
        else:
            player.batting_stats = self.get_batting_stats(player)
            player.batting_ratings = self.get_batting_ratings(player)
        player.retired = self.get_retired()
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

    def get_batting_ratings(self, player):
        pass

    def get_pitching_ratings(self, player):
        pass

    def get_retired(self):
        pass

    def get_table_value(self, soup, key):
        return soup.find(text=re.compile(key)).parent.next_sibling.text