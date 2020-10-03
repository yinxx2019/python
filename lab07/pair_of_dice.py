from die import Die


class PairOfDice:
    '''roll both dices'''
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def roll_dice(self):
        self.die1.roll()
        self.die2.roll()

    def current_value(self):
        return self.die1.current_value + self.die2.current_value
