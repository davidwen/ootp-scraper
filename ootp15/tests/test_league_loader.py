from ootp15.league_loader import LeagueLoader

import unittest

class TestLeagueLoader(unittest.TestCase):

    def setUp(self):
        self.league = LeagueLoader().load_league(100)
        self.minor_league = LeagueLoader().load_league(105)

    def test_id(self):
        self.assertEqual(self.league.id, 100)
        self.assertEqual(self.minor_league.id, 105)

    def test_name(self):
        self.assertEqual(self.league.name, 'United States Baseball League')
        self.assertEqual(self.minor_league.name, 'CUB Primary Affiliation')

    def test_teams(self):
        self.assertEqual(len(self.league.team_ids), 8)
        self.assertEqual(len(self.minor_league.team_ids), 8)

    def test_load_all(self):
        self.assertEqual(len(LeagueLoader().load_all()), 28)