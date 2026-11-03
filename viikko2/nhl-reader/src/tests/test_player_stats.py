"""Unit tests for PlayerStats."""

import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    """Provide sample players without making network requests."""

    def get_players(self):
        """Return the sample players used by the tests."""
        return [
            Player({
                "name": "Player One",
                "nationality": "FIN",
                "team": "BOS",
                "goals": 10,
                "assists": 5,
            }),
            Player({
                "name": "Player Two",
                "nationality": "USA",
                "team": "BOS",
                "goals": 8,
                "assists": 10,
            }),
            Player({
                "name": "Player Three",
                "nationality": "FIN",
                "team": "NYR",
                "goals": 20,
                "assists": 0,
            }),
            Player({
                "name": "Player Four",
                "nationality": "FIN",
                "team": "BOS",
                "goals": 7,
                "assists": 3,
            }),
        ]


class TestPlayerStats(unittest.TestCase):
    """Test player filtering and sorting operations."""

    def setUp(self):
        """Create a PlayerStats instance backed by the local stub."""
        self.stats = PlayerStats(PlayerReaderStub())

    def test_top_scorers_by_nationality_filters_and_sorts_by_points(self):
        """Filter players by nationality and sort by descending points."""
        players = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(
            [player.name for player in players],
            ["Player Three", "Player One", "Player Four"],
        )

    def test_top_scorers_by_team_filters_and_sorts_by_points(self):
        """Filter players by team and sort by descending points."""
        players = self.stats.top_scorers_by_team("BOS")

        self.assertEqual(
            [player.name for player in players],
            ["Player Two", "Player One", "Player Four"],
        )

    def test_top_goal_scorers_returns_requested_number_in_goal_order(self):
        """Return only the requested number of players sorted by goals."""
        players = self.stats.top_goal_scorers(2)

        self.assertEqual(
            [player.name for player in players],
            ["Player Three", "Player One"],
        )
