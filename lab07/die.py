import random as r


class Die:
    '''get current value of dice'''

    def __init__(self):
        self.current_value = 0

    def roll(self):
        self.current_value = r.randint(1, 6)
