from ootp15.team_loader import TeamLoader

import unittest

class TestTeamLoader(unittest.TestCase):

    def setUp(self):
        self.team = TeamLoader(430).team
        self.ml_team = TeamLoader(623).team

    def test_id(self):
        self.assertEqual(self.team.id, 430)

    def test_name(self):
        self.assertEqual(self.team.name, 'Thetford Mines Settlers')

    def test_level(self):
        self.assertEqual(self.team.level, 'AAA')

    def test_parent_team_id(self):
        self.assertEqual(self.team.parent_team_id, 422)

    def test_count(self):
        self.assertEqual(len(self.ml_team.player_positions), 25)