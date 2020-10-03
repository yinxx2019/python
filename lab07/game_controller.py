from pair_of_dice import PairOfDice


class GameController:
    '''game controller for the dice game'''
    def __init__(self):
        self.pair_of_dice = PairOfDice()
    print("-------------------------")
    print("Welcome to street craps!")
    print("If you roll 7 or 11 on your first roll, you win.")
    print("If you roll 2, 3, or 12 on your first role, you lose.")
    print("If you roll anything else, that's your 'point', and")
    print("you keep rolling until you either roll your point")
    print("again (win) or roll a 7 (lose)")
    enter = input("Press enter to roll the dice...")

    def situations(self):
        WIN = [7, 11]
        LOSE = [2, 3, 12]
        SEVEN = 7
        # situation: win at the first time
        if (self.pair_of_dice.current_value() in WIN):
            print("You rolled", str(self.pair_of_dice.current_value()) +
                  ". You Win!")
        # situation: lose at the first time
        elif (self.pair_of_dice.current_value() in LOSE):
            print("You rolled", str(self.pair_of_dice.current_value()) +
                  ". You Lose.")
        # situation: roll until same point or magic num 7
        else:
            print("Your point is", self.pair_of_dice.current_value())
            point = self.pair_of_dice.current_value()
            self.pair_of_dice.roll_dice()
            while self.pair_of_dice.current_value() != point:
                enter = input("Press enter to roll the dice...")
                self.pair_of_dice.roll_dice()
                print("You rolled", self.pair_of_dice.current_value())
                if self.pair_of_dice.current_value() == SEVEN:
                    print("You rolled", str(self.pair_of_dice.current_value())
                          + ". You Lose.")
                    break
            else:
                print("You rolled", str(self.pair_of_dice.current_value()) +
                      ". You Win!")
        # I will revisit this part to try to put win/lose/continue rolling
        # situations in three objects once I learned more OOD

    def start_play(self):
        self.pair_of_dice.roll_dice()
        self.situations()
