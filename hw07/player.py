

class Player:
    """A class representing a dodgeball player"""
    def __init__(self):
        self.player_name = 0
        self.player_number = 0
        self.player_position = 0

    def add(self, player_name, player_number, player_position):
        """add players and their info"""
        self.player_name = player_name
        self.player_number = player_number
        self.player_position = player_position
        return [self.player_name, self.player_number, self.player_position]

    def position_check(self, player_position):
        """return player positons for checking"""
        return self.player_position

    def name_check(self, player_name):
        """return player names"""
        return self.player_name
