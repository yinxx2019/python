from player import Player


class Team:
    """A class representing a dodgeball team"""
    # All methods in Python include arguments representing the object
    # itself. In the method definition, this is represented by the
    # `self` parameter.
    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []
        self.player = Player()
        self.all_positions = []
        self.all_names = []

    # Another example of self. The method call only passes one argument,
    # the 'name; value. But the method definition must always include the
    # self parameter.

    def set_team_name(self, name):
        self.name = name

    # Note again that `self` is the first parameter.
    def add_player(self, player_name, player_number, player_position):
        # call the Player class constructor with the appropriate
        # values to create a new player object, then add that
        # player object to the team's players list.
        self.players.append(self.player.add(player_name, player_number,
                            player_position))
        return self.players

    def add_position(self, player_position):
        self.all_positions.append(self.player.position_check(player_position))
        return self.all_positions

    def add_name(self, player_name):
        self.all_names.append(self.player.name_check(player_name))
        return self.all_names

    def cut_player(self, player_name):
        # Remove the player with the name player_name from the players list.
        if player_name in self.all_names:
            for i in self.players:
                if player_name in i:
                    self.players.remove(i)
                    self.all_positions.remove(i[2])
                    self.all_names.remove(player_name)
            print(player_name, "has been cut from", self.name)
        else:
            print(player_name, "is not on the team")
            return self.all_names

    def is_position_filled(self, position):
        # Write the method that checks whether there is currently at least one
        # player on the team occupying the requested position
        self.position = position
        if self.position in self.all_positions:
            print("Yes, the", self.position, "position is filled")
        else:
            print("No, the", self.position, "position is not filled")

    # Write any necessary methods to support the methods
    # above, and write the method that will display (print to screen)
    # the full team roster in the following format:

    def show_team_roster(self):
        # first test if there's any players
        if len(self.players) != 0:
            for i in self.players:
                # swap number and name
                i[0], i[1] = i[1], i[0]
            print("The lineup for", self.name, "is")
            for row in self.players:
                print("{: <10}{: <10}{: <10}".format(*row))
            for i in self.players:
                # swap back after printing the message that helps format
                i[0], i[1] = i[1], i[0]
        else:
            print(self.name, "is empty")
