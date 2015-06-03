import re

from models import pitcher_ratings
from loaders import loader

class PitcherRatingsLoader(loader.Loader):

    def __init__(self, soup, player):
        self.soup = soup
        self.player = player
        self.values = self.get_values()
        self.ratings = self.load_ratings()
        loader.Loader.__init__(self)

    def load_ratings(self):
        ratings = pitcher_ratings.PitcherRatings()
        ratings.player_id = self.player.id
        ratings.stuff = self.get_stuff()
        ratings.movement = self.get_movement()
        ratings.control = self.get_control()
        ratings.stuff_l = self.get_stuff_l()
        ratings.movement_l = self.get_movement_l()
        ratings.control_l = self.get_control_l()
        ratings.stuff_r = self.get_stuff_r()
        ratings.movement_r = self.get_movement_r()
        ratings.control_r = self.get_control_r()
        ratings.pot_stuff = self.get_pot_stuff()
        ratings.pot_movement = self.get_pot_movement()
        ratings.pot_control = self.get_pot_control()
        ratings.stamina = self.get_stamina()
        ratings.velocity = self.get_velocity()
        ratings.hold = self.get_hold()
        ratings.groundball = self.get_groundball()
        return ratings

    def convert_value(self, value):
        if value == '-' or value == '':
            return 0
        else:
            return int(value)

    def get_values(self):
        return [self.convert_value(td.text) for td in self.soup.find_all('td', class_='dc')[14:26]]

    def get_table_value(self, key):
        return self.soup.find(text=re.compile(key)).parent.next_sibling.next_sibling.text

    def get_stuff(self):
        return self.values[0]

    def get_movement(self):
        return self.values[4]

    def get_control(self):
        return self.values[8]

    def get_stuff_l(self):
        return self.values[1]

    def get_movement_l(self):
        return self.values[5]

    def get_control_l(self):
        return self.values[9]

    def get_stuff_r(self):
        return self.values[2]

    def get_movement_r(self):
        return self.values[6]

    def get_control_r(self):
        return self.values[10]

    def get_pot_stuff(self):
        return self.values[3]

    def get_pot_movement(self):
        return self.values[7]

    def get_pot_control(self):
        return self.values[11]

    def get_stamina(self):
        return self.convert_value(self.get_table_value('Stamina'))

    def get_velocity(self):
        return self.convert_value(self.get_table_value('Velocity').split(' ')[0].split('-')[1])

    def get_hold(self):
        return self.convert_value(self.get_table_value('Hold Runners'))

    def get_groundball(self):
        return self.convert_value(self.get_table_value('Groundball Percentage').split(' ')[0])
