class PlayerStats:
    def __init__(self, reader):
        self._reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self._reader.get_players()
        matching = [p for p in players if p.nationality == nationality]
        return sorted(matching, key=lambda p: p.points, reverse=True)