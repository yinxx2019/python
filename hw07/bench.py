

class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        # Initialize the bench object with attributes and values it will need
        self.bench = []

    def send_to_bench(self, player_name):
        # Put the player "onto the bench"
        self.player_name = player_name
        self.bench.append(self.player_name)
        return self.bench

    def get_from_bench(self):
        if len(self.bench) != 0:
            print("Got", self.bench[0], "from bench")
            self.bench.remove(self.bench[0])
        else:
            print("The bench is empty.")

    def show_bench(self):
        # function that will display the current list of players on the bench
        if len(self.bench) != 0:
            print("The bench currently includes:")
            for i in self.bench:
                print(i)
        else:
            print("The bench is empty.")

    def cut_bench(self, player_name):
        self.player_name = player_name
        self.bench.remove(self.player_name)
        return self.bench
