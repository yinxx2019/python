from stack import Stack


class StringProcessor:
    """Class for processing strings"""
    def __init__(self):
        self.stack = Stack()
        self.asterisk = "*"
        self.caret = "^"
        self.solution = ""

    def process_string(self, line):
        # create the stack
        for i in line:
            if i != self.asterisk and i != self.caret:
                self.stack.items.append(i)
            elif i == self.asterisk:
                # pop from stack and add to solution when meet asterisk
                if self.stack.peek() is not None:
                    self.solution += self.stack.peek()
                    self.stack.pop()
            elif i == self.caret:
                # pop and append twice
                if self.stack.peek() is not None:
                    self.solution += self.stack.peek()
                    self.stack.pop()
                    self.solution += self.stack.peek()
                    self.stack.pop()
        return self.solution
