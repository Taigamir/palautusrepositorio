"""Module that defines the dataform Player"""

class Player:
    """Class that sorts data into separate players"""
    def __init__(self, player_dict):
        """initiates by splitting data into categories"""
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.team = player_dict['team']
        self.goals = player_dict['goals']
        self.assists = player_dict['assists']

    @property
    def points(self):
        """Creates new statistic points"""
        return self.goals + self.assists

    def __str__(self):
        """Formats the data for printing"""
        return (f"{self.name:20} team {self.team:15} "
                f"{self.goals:2} + {self.assists:2} = {self.points:3}")
