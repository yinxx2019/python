from team import Team
from bench import Bench


def main():
    '''team management system that trigger a series of function under
    team class and bench class'''
    print("Welcome to the team manager.")
    # Here's where we create objects for the team and the bench. These
    # objects will be able to call the methods we've defined in their
    # respective classes. When the constructor functions are called here,
    # the classes' __init__() method is called with these values
    # passed to it. In both of these cases no arguments are passed, here.
    # However, the `self` argument is always implicitly passed with any
    # method call.
    the_team = Team()
    the_bench = Bench()

    while True:
        # Immediately converting the input to lower() lets the user enter
        # any kind of capitalization, so it's a little less strict.
        command = (input("What do you want to do?\n")).lower()

        if command == "done":
            print("Shutting down team manager\n")
            return  # this return statement exits main, ending the session.
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_team, the_bench)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
        elif command == "cut player":
            # call a function that calls the appropriate method on the team
            # object to cut the player (you need to write the function below)
            do_cut_player(the_team, the_bench)
        elif command == "show bench":
            # call a function to call the necessary bench method to show the
            # names of the players who are currently on the bench.
            do_show_bench(the_bench)
        else:
            do_not_understand()


def do_set_team_name(team):
    name = input("What do you want to name the team?\n")
    # check if team name contains only alphanumeric characters and spaces
    while all(x.isalnum() or x.isspace() for x in name) is False:
        print("Enter a team name with alphanumeric characters and spaces")
        name = input("What do you want to name the team?\n")
    team.set_team_name(name)


def do_show_team_roster(team):
    # call the method on the team object that displays the roster
    team.show_team_roster()


def do_check_position_filled(team):
    position = input("What position are you checking for?\n")
    # call the method on the team object that determines
    # whether a given position has at least one player filling it, then print
    # the appropriate message:  "Yes, the", position, "position is filled" or
    # "No, the", position, "position is not filled"
    team.is_position_filled(position)


def do_add_player_to_team(team):
    player_name = input("What's the player's name?\n")
    # check if player name contains only alphanumeric characters and spaces
    while all(x.isalnum() or x.isspace() for x in player_name) is False:
        print("Enter a player name with alphanumeric Characters and Spaces")
        player_name = input("What's the player's name?\n")
    player_number = input("What's " + player_name + "'s number?\n")
    # check if player number contains only digits
    while all(x.isdigit() for x in player_number) is False:
        print("Enter a player number with only integers")
        player_number = input("What's " + player_name + "'s number?\n")
    player_position = input("What's " + player_name + "'s position?\n")
    team.add_player(player_name, player_number, player_position)
    team.add_position(player_position)
    team.add_name(player_name)
    print("Added", player_name, "to", team.name)


def do_cut_player(team, bench):
    player_name = input("Who do you want to cut?\n")
    # call the method on team that creates a new player and
    # adds the player to the team.
    team.cut_player(player_name)
    # cut player from bench if he is on bench
    if player_name in bench.bench:
        bench.cut_bench(player_name)


def do_send_player_to_bench(team, bench):
    name = input("Who do you want to send to the bench?\n")
    # make sure that the player is actually on the team first
    if name in team.all_names:
        # first check if the player is already on the bench
        if name in bench.bench:
            print(name, "is already on the bench")
        else:
            # and then call a method on the bench object to place the player
            bench.send_to_bench(name)
            print("Sent", name, "to bench.")
    else:
        print(name, "is not on the team")


def do_get_player_from_bench(bench):
    # get the best-rested player by name from the bench
    # Print to the screen the name of the player who was retrieved from the
    # bench. If the bench is empty, print it.
    bench.get_from_bench()


def do_show_bench(bench):
    # write a function to call the necessary method to show the
    # names of the players who are currently on the bench.
    bench.show_bench()


def do_not_understand():
    print("I didn't understand that command")


main()
