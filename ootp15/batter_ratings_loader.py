import re

from models import batter_ratings

class BatterRatingsLoader():

    def __init__(self, soup, player):
        self.soup = soup
        self.player = player
        self.values = self.get_values()
        self.ratings = self.load_ratings()

    def load_ratings(self):
        ratings = batter_ratings.BatterRatings()
        ratings.player_id = self.player.id
        ratings.contact = self.get_contact()
        ratings.gap = self.get_gap()
        ratings.power = self.get_power()
        ratings.eye = self.get_eye()
        ratings.avoid_k = self.get_avoid_k()
        ratings.contact_r = self.get_contact_r()
        ratings.gap_r = self.get_gap_r()
        ratings.power_r = self.get_power_r()
        ratings.eye_r = self.get_eye_r()
        ratings.avoid_k_r = self.get_avoid_k_r()
        ratings.contact_l = self.get_contact_l()
        ratings.gap_l = self.get_gap_l()
        ratings.power_l = self.get_power_l()
        ratings.eye_l = self.get_eye_l()
        ratings.avoid_k_l = self.get_avoid_k_l()
        ratings.pot_contact = self.get_pot_contact()
        ratings.pot_gap = self.get_pot_gap()
        ratings.pot_power = self.get_pot_power()
        ratings.pot_eye = self.get_pot_eye()
        ratings.pot_avoid_k = self.get_pot_avoid_k()
        return ratings

    def get_values(self):
        return [int(td.text) for td in self.soup.find_all('td', class_='dc')[14:38] if td.text]

    def get_contact(self):
        return self.values[0]

    def get_gap(self):
        return self.values[4]

    def get_power(self):
        return self.values[8]

    def get_eye(self):
        return self.values[12]

    def get_avoid_k(self):
        return self.values[16]

    def get_contact_r(self):
        return self.values[2]

    def get_gap_r(self):
        return self.values[6]

    def get_power_r(self):
        return self.values[10]

    def get_eye_r(self):
        return self.values[14]

    def get_avoid_k_r(self):
        return self.values[18]

    def get_contact_l(self):
        return self.values[1]

    def get_gap_l(self):
        return self.values[5]

    def get_power_l(self):
        return self.values[9]

    def get_eye_l(self):
        return self.values[13]

    def get_avoid_k_l(self):
        return self.values[17]

    def get_pot_contact(self):
        return self.values[3]

    def get_pot_gap(self):
        return self.values[7]

    def get_pot_power(self):
        return self.values[11]

    def get_pot_eye(self):
        return self.values[15]

    def get_pot_avoid_k(self):
        return self.values[19]