from extra_credit import ExtraCredit
from word_ladder import WordLadder
from stack import Stack


def main():
    """Run an interactive command line to let the user
    input word pairs and generate word ladders"""
    english_words = load_words()

    while True:
        w1, w2 = input("> ").split()
        if len(w1) == len(w2):
            # Everything same with word_ladder_app
            wl = WordLadder(w1, w2, english_words[len(w1)])
            word_ladder = wl.make_ladder()
            print("Ladder: ", word_ladder)
        else:
            # a set of words for adding later
            check_words_set = set()
            diff = abs(len(w1) - len(w2))
            initial_insertion = "a"
            if len(w1) < len(w2):
                shorter = len(w1)
                longer = len(w2)
                start = w1
                end = w2
            else:
                shorter = len(w2)
                longer = len(w1)
                start = w2
                end = w1
            # add words with length in range of shorter to longer
            for i in range(shorter, longer+1):
                for j in english_words[i]:
                    check_words_set.add(j)
            ec = ExtraCredit(start, end, check_words_set)
            word_ladder = ec.make_ladder()
            # normal print if start with w1
            if start == w1:
                print("Ladder: ", word_ladder)
            # reverse if start with w2
            elif start == w2:
                print("Ladder: ", reverse_ladder(word_ladder))


def load_words():
    """Load words from complete wordlist file"""
    # We're creating a dictionary keyed on word
    # length, so that we can quickly get to a set of
    # words of a given length.
    valid_words = {}
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            if len(w) in valid_words.keys():
                # Add to an existing set
                valid_words[len(w)].add(w)
            else:
                # Initialize a set with one element
                valid_words[len(w)] = {w}
    return valid_words


def reverse_ladder(word_ladder):
    '''reverse the order of word ladder stack'''
    tmp1 = Stack()
    while not word_ladder.isEmpty():
        tmp1.push(word_ladder.pop())
    tmp2 = Stack()
    while not tmp1.isEmpty():
        tmp2.push(tmp1.pop())
    while not tmp2.isEmpty():
        word_ladder.push(tmp2.pop())
    return word_ladder


main()
