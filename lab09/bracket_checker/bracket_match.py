from stack import Stack


class BracketMatch:
    """Class for evaluating parenthetical strings"""
    # Implement bracket matching functionality as required
    def __init__(self):
        self.open_list = ["(", "[", "{"]
        self.close_list = [")", "]", "}"]
        self.stack = Stack()

    def brackets_match(self, line):
        for i in line:
            if i in self.open_list:
                self.stack.push(i)  # add open brackets to stack
            elif i in self.close_list:
                bracket = self.close_list.index(i)
                # check if there are open brackets have been added
                if len(self.stack.items) == 0:
                    return False
                # remove matching open brackets from the list
                elif self.open_list[bracket] == self.stack.peek():
                    self.stack.pop()  # remove corresponding open bracket
        if len(self.stack.items) == 0:  # all open brackets have been matched
            return True
        else:
            return False
