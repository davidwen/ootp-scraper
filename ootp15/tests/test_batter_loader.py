from ootp15.player_loader import PlayerLoader

import unittest

class TestBatterLoader(unittest.TestCase):

    def setUp(self):
        self.player = PlayerLoader(7247).player

    def test_id(self):
        self.assertEqual(self.player.id, 7247)

    def test_name(self):
        self.assertEqual(self.player.name, 'Munenori Ishihara')

    def test_birthday(self):
        self.assertEqual(self.player.birthday, '04/03/2001')

    def test_leadership(self):
        self.assertEqual(self.player.leadership, 2)

    def test_loyalty(self):
        self.assertEqual(self.player.loyalty, 3)

    def test_desire_for_win(self):
        self.assertEqual(self.player.desire_for_win, 4)

    def test_greed(self):
        self.assertEqual(self.player.greed, 2)

    def test_intelligence(self):
        self.assertEqual(self.player.intelligence, 4)

    def test_work_ethic(self):
        self.assertEqual(self.player.work_ethic, 5)

    def test_bats(self):
        self.assertEqual(self.player.bats, 'L')

    def test_throws(self):
        self.assertEqual(self.player.throws, 'L')

    def test_position(self):
        self.assertEqual(self.player.position, 'LF')

    def test_ratings(self):
        ratings = self.player.batting_ratings
        self.assertEquals(ratings.contact, 8)
        self.assertEquals(ratings.gap, 7)
        self.assertEquals(ratings.power, 9)
        self.assertEquals(ratings.eye, 6)
        self.assertEquals(ratings.avoid_k, 6)
        self.assertEquals(ratings.contact_r, 8)
        self.assertEquals(ratings.gap_r, 7)
        self.assertEquals(ratings.power_r, 9)
        self.assertEquals(ratings.eye_r, 7)
        self.assertEquals(ratings.avoid_k_r, 6)
        self.assertEquals(ratings.contact_l, 7)
        self.assertEquals(ratings.gap_l, 6)
        self.assertEquals(ratings.power_l, 7)
        self.assertEquals(ratings.eye_l, 5)
        self.assertEquals(ratings.avoid_k_l, 5)
        self.assertEquals(ratings.pot_contact, 8)
        self.assertEquals(ratings.pot_gap, 7)
        self.assertEquals(ratings.pot_power, 9)
        self.assertEquals(ratings.pot_eye, 7)
        self.assertEquals(ratings.pot_avoid_k, 6)

    def test_batting_stats(self):
        self.assertEqual(len(self.player.batting_stats), 16)
        self.assertEqual(len([stat for stat in self.player.batting_stats if stat.team_id == 32]), 3)
        self.assertEqual(self.player.career_positions[(2026, 191)], 'CF')

    def test_retired(self):
        self.assertEquals(self.player.retired, False)