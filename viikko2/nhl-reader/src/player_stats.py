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
