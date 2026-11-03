"""Module for formatting and sorting data"""

class PlayerStats:
    """Class allows for the manipulation of playerstats"""
    def __init__(self, reader):
        """initialise the class"""
        self._reader = reader

    def top_scorers_by_nationality(self, nationality):
        """Funtion sorts the players of requested nation by points"""
        players = self._reader.get_players()
        matching = [p for p in players if p.nationality == nationality]
        return sorted(matching, key=lambda p: p.points, reverse=True)

    def top_scorers_by_team(self, team):
        """Sorts the players of the requested team by points"""
        players = self._reader.get_players()
        matching = [p for p in players if p.team == team]
        return sorted(matching, key=lambda p: p.points, reverse=True)

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa"""
        players = self._reader.get_players()
        return sorted(players, key=lambda p: p.goals, reverse=True)[:how_many]
