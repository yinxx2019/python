from flying_object import FlyingObject

# Problem 3, Part 1: Laser beam lifespans
#
# Implement laser beam lifespan and whatever
# further logic is needed to ensure that the
# laser beam's remaining lifespan is updated
# with each frame. You may make changes anywhere
# in this class definition.

# Set the lifespan to a default of 100 frames.


class LaserBeam(FlyingObject):
    """A single laser torpedo"""
    def __init__(self, SPACE, x, y, x_vel, y_vel, lifespan):
        self.LASER_SPEED_FACTOR = 5
        self.SPACE = SPACE
        self.rotation = 0.0
        self.radius = 2.5
        self.diam = self.radius*2
        self.x_vel = x_vel * self.LASER_SPEED_FACTOR
        self.y_vel = y_vel * self.LASER_SPEED_FACTOR
        self.x = x + x_vel
        self.y = y + y_vel
        # Problem 3, Part 1, value passed by game_controller
        self.lifespan = lifespan

    def draw_me(self):
        FILL_COLOR = 1
        fill(FILL_COLOR)
        noStroke()
        ellipse(0, 0, self.diam, self.diam)
