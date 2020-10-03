from queue import Queue
from stack import Stack


class ExtraCredit:
    """A class providing functionality to create word ladders"""
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.
    def __init__(self, w1, w2, wordlist):
        self.w1 = w1.lower()
        self.w2 = w2.lower()
        self.wordlist = wordlist  # pass the value of valid_words
        self.stack = Stack()
        self.queue = Queue()
        self.alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                         "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                         "u", "v", "w", "x", "y", "z"}
        # set for combo alphabet
        self.combo = set()
        # set for all checked candidates
        self.checked = set()

    def make_ladder(self):
        # adding items to combo alphabet
        for i in self.alphabet:
            self.combo.add(i)
            for j in self.alphabet:
                self.combo.add(i+j)
        # a single stack contains the first word in the word ladder
        self.stack.push(self.w1)
        # initialize a queue containing the stack above
        self.queue.enqueue(self.stack)
        # for each element in the queue
        while self.queue.size() > 0:
            # dequeue the element which is a stack
            word_stack = self.queue.dequeue()
            # peek at its top item (a word)
            word = word_stack.peek()
            for character in range(0, len(word)):
                for letter in self.combo:
                    # replace the character to generate a candidate new word
                    if word[character] != letter:
                        cddt = word[:character] + letter + word[character+1:]
                        # check the candidate to see if it is an English word
                        if cddt in self.wordlist and cddt not in self.checked:
                            # duplicate stack and push onto new stack
                            new_stack = word_stack.copy()
                            new_stack.push(cddt)
                            self.checked.add(cddt)
                            # if the word is the last word of the word ladder
                            if cddt == self.w2:
                                return new_stack
                            elif cddt != self.w2:
                                self.queue.enqueue(new_stack)
        # if self.queue.isEmpty():
        return None
