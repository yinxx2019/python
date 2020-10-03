class Point:
    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y

    def getX(self):
        return self.xCoord

    def getY(self):
        return self.yCoord

    def midPoint(self, otherPoint):
        # calculate the coordinates of the new midpoint.
        newX = float((self.xCoord + otherPoint.xCoord) / 2)
        newY = float((self.yCoord + otherPoint.yCoord) / 2)
        return Point(newX, newY)
