"""Program for pulling data from online"""
import requests
from player import Player

class PlayerReader:
    """Class that reads website data and transfers it into readable format"""
    def __init__(self, url):
        """Initialise required data for read class"""
        self._url = url

    def get_players(self):
        """Function pulls for requested data and converts to list"""
        response = requests.get(self._url, timeout=10).json()
        return [Player(player_dict) for player_dict in response]
