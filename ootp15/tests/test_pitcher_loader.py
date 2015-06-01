from ootp15.player_loader import PlayerLoader

import unittest

class TestPitcherLoader(unittest.TestCase):

    def setUp(self):
        self.player = PlayerLoader(2312).player

    def test_id(self):
        self.assertEqual(self.player.id, 2312)

    def test_name(self):
        self.assertEqual(self.player.name, 'Braydon Hughes')

    def test_birthday(self):
        self.assertEqual(self.player.birthday, '05/24/2006')

    def test_leadership(self):
        self.assertEqual(self.player.leadership, 3)

    def test_loyalty(self):
        self.assertEqual(self.player.loyalty, 5)

    def test_desire_for_win(self):
        self.assertEqual(self.player.desire_for_win, 4)

    def test_greed(self):
        self.assertEqual(self.player.greed, 3)

    def test_intelligence(self):
        self.assertEqual(self.player.intelligence, 3)

    def test_work_ethic(self):
        self.assertEqual(self.player.work_ethic, 4)

    def test_bats(self):
        self.assertEqual(self.player.bats, 'L')

    def test_throws(self):
        self.assertEqual(self.player.throws, 'R')

    def test_position(self):
        self.assertEqual(self.player.position, 'MR')

    def test_pitching_stats(self):
        self.assertEquals(len(self.player.pitching_stats), 10)
        self.assertEquals(len([stat for stat in self.player.pitching_stats if stat.team_id == 488]), 8)

    def test_pitching_ratings(self):
        ratings = self.player.pitching_ratings
        self.assertEquals(ratings.stuff, 7)
        self.assertEquals(ratings.movement, 6)
        self.assertEquals(ratings.control, 8)
        self.assertEquals(ratings.stuff_l, 7)
        self.assertEquals(ratings.movement_l, 6)
        self.assertEquals(ratings.control_l, 7)
        self.assertEquals(ratings.stuff_r, 7)
        self.assertEquals(ratings.movement_r, 6)
        self.assertEquals(ratings.control_r, 8)
        self.assertEquals(ratings.pot_stuff, 7)
        self.assertEquals(ratings.pot_movement, 6)
        self.assertEquals(ratings.pot_control, 8)
        self.assertEquals(ratings.stamina, 7)
        self.assertEquals(ratings.velocity, 91)
        self.assertEquals(ratings.hold, 3)
        self.assertEquals(ratings.groundball, 59)

    def test_retired(self):
        self.assertEquals(self.player.retired, False)