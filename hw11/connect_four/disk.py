class Disk:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.active = False
        self.hide = False
        self.rate = 1
        self.radius = 50
        # when the disk is generated but not falling, set position to be -1
        # if it falls to bottom, position will be 0.
        self.position = -1

    def display(self):
        if self.hide:
            return
        noStroke()
        fill(self.color)
        ellipse(self.x, self.y, 100, 100)
