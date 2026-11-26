POINT_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
TIE_SCORE_NAMES = ["Love-All", "Fifteen-All", "Thirty-All"]
DEUCE_LABEL = "Deuce"
ENDGAME_THRESHOLD = 4
ADVANTAGE_MARGIN = 1
WIN_MARGIN = 2

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points = self.player1_points + 1
        else:
            self.player2_points = self.player2_points + 1

    def get_score(self):
        if self.player1_points == self.player2_points:
            return self._tie_score()

        if max(self.player1_points, self.player2_points) >= ENDGAME_THRESHOLD:
            return self._endgame_score()
        return (
            self._point_name(self.player1_points)
            + "-"
            + self._point_name(self.player2_points)
        )

    def _tie_score(self):
        if self.player1_points < len(TIE_SCORE_NAMES):
            return TIE_SCORE_NAMES[self.player1_points]
        return DEUCE_LABEL

    def _point_name(self, points):
        return POINT_NAMES[points]

    def _endgame_score(self):
        lead = self.player1_points - self.player2_points

        if abs(lead) >= WIN_MARGIN:
            return self._win_score(lead)
        return self._advantage_score(lead)

    def _advantage_score(self, lead):
        if lead > 0:
            return f"Advantage {self.player1_name}"
        else:
            return f"Advantage {self.player2_name}"

    def _win_score(self, lead):
        if lead > 0:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"
