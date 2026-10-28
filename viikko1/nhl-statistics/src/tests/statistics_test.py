import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_player(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_returns_None_for_player(self):
        self.assertIsNone(self.stats.search("Nobody"))

    def test_team_returns_only_that_teams_players(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)

    def test_top_places_best_player_first(self):
        top = self.stats.top(1)
        self.assertEqual(top[0].name, "Gretzky")

    def test_top_works_by_goals(self):
        top = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(top[0].name, "Lemieux")

    def test_top_works_by_assists(self):
        top = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(top[0].name, "Gretzky")

    def test_top_works_by_points(self):
        top = self.stats.top(1, SortBy.POINTS)
        self.assertEqual(top[0].name, "Gretzky")

