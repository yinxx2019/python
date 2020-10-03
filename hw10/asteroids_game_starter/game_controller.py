from laserbeam import LaserBeam
from asteroid import Asteroid
from spaceship import Spaceship


class GameController:
    """
    Maintains the state of the game
    and manages interactions of game elements.
    """

    def __init__(self, SPACE, fadeout):
        """Initialize the game controller"""
        self.SPACE = SPACE
        self.fadeout = fadeout

        self.spaceship_hit = False
        self.asteroid_destroyed = False
        self.asteroids = [Asteroid(self.SPACE)]
        self.laser_beams = []
        self.spaceship = Spaceship(self.SPACE)
        # Problem 3: set lifespan for passing to laserbeam class
        self.lifespan = 100
        # magic number for laser beam run out of lifespan
        self.DIE = 0

    def update(self):
        """Updates game state on every frame"""
        self.do_intersections()

        for asteroid in self.asteroids:
            asteroid.display()
        # ======================================================
        # Problem 3, Part 2: Laser beam handler
        # Your code will replace (or augment) the next several
        # lines. Laser beam objects should remain in the scene
        # as many frames as their lifespan allows.
        # Begin problem 3 code changes

        for l in range(len(self.laser_beams)):
            if self.laser_beams[l].lifespan > self.DIE:
                self.laser_beams[l].display()
                self.laser_beams[l].lifespan -= 1

        # End problem 3, part 2 code changes
        # =======================================================

        self.spaceship.display()

        # Carries out necessary actions if game over
        if self.spaceship_hit:
            if self.fadeout <= 0:
                fill(1)
                textSize(30)
                text("YOU HIT AN ASTEROID",
                     self.SPACE['w']/2 - 165, self.SPACE['h']/2)
            else:
                self.fadeout -= 1

        if self.asteroid_destroyed:
            fill(1)
            textSize(30)
            text("YOU DESTROYED THE ASTEROIDS!!!",
                 self.SPACE['w']/2 - 250, self.SPACE['h']/2)

    def fire_laser(self, x, y, rot):
        """Add a laser beam to the game"""
        x_vel = sin(radians(rot))
        y_vel = -cos(radians(rot))
        self.laser_beams.append(
            LaserBeam(self.SPACE, x, y, x_vel, y_vel, self.lifespan)
            )

    def handle_keypress(self, key, keycode=None):
        if (key == ' '):
            if self.spaceship.intact:
                self.spaceship.control(' ', self)
        if (keycode):
            if self.spaceship.intact:
                self.spaceship.control(keycode)

    def handle_keyup(self):
        # problem 2: delete the wrong condition
        # if not self.spaceship.intact:
        self.spaceship.control('keyup')

    def do_intersections(self):
        # ======================================================
        # Problem 4, Part 1: Intersections
        # Here's where you'll probably want to check for intersections
        # between asteroids and laser beams. Laser beams should be removed
        # from the scene if they hit an asteroid, and the asteroid should
        # blow up (the blow_up_asteroid method also must be written. It's
        # been started for you below).
        # The intersection logic below between the spaceship
        # and asteroids should give a hint as to how this will work.
        # Begin code changes for Problem 4, Part 1: Intersections
        if len(self.asteroids) == 0:
            self.asteroid_destroyed = True
        else:
            for asteroid in self.asteroids:
                for beam in self.laser_beams:
                    if (
                            abs(beam.x - asteroid.x) <
                            max(asteroid.radius, beam.radius)
                            and
                            abs(beam.y - asteroid.y) <
                            max(asteroid.radius, beam.radius)
                            # make sure that the laser beam is active
                            and beam.lifespan > self.DIE):
                        # end the lifespan of laser beam after intersection
                        beam.lifespan = self.DIE
                        # call blow_up_asteroid function
                        self.blow_up_asteroid(asteroid, beam)
        # End of code changes for Problem 4, Part 1: Intersections
        # ======================================================

        # If the space ship still hasn't been blown up
        if self.spaceship.intact:
            # Check each asteroid for intersection
            for i in range(len(self.asteroids)):
                if (
                      abs(self.spaceship.x - self.asteroids[i].x)
                      < max(self.asteroids[i].radius, self.spaceship.radius)
                      and
                      abs(self.spaceship.y - self.asteroids[i].y)
                      < max(self.asteroids[i].radius, self.spaceship.radius)):
                    # We've intersected an asteroid
                    self.spaceship.blow_up(self.fadeout)
                    self.spaceship_hit = True

    def blow_up_asteroid(self, i, j):
        # ======================================================
        # Problem 4, Part 2: Asteroid blow-up
        # Begin code changes for Problem 4, Part 2: Asteroid blow-up

        # slow down the speed of asteroids pieces
        speed_factor = 0.5
        # I understand that usually we don't name item using index,
        # but I find using item instead of index in the loop is much more
        # efficient and I don't want to change names in starter's code
        if i.asize == 'Large':
            # B) Add appropriate smaller asteroids to the scene
            # Specifically. If the large asteroid is hit, it should
            # break into two medium asteroids, which should fly off
            # perpendicularly to the direction of the laser beam.
            piece_1 = Asteroid(self.SPACE)
            piece_1.asize = 'Med'
            # C) Make sure that the smaller asteroids are positioned
            # correctly and flying off in the correct directions
            piece_1.x = i.x
            piece_1.y = i.y
            piece_1.x_vel = - j.x_vel * speed_factor
            piece_1.y_vel = j.y_vel * speed_factor
            self.asteroids.append(piece_1)
            piece_2 = Asteroid(self.SPACE)
            piece_2.asize = 'Med'
            piece_2.x = i.x
            piece_2.y = i.y
            piece_2.x_vel = j.x_vel * speed_factor
            piece_2.y_vel = - j.y_vel * speed_factor
            self.asteroids.append(piece_2)
            # A) Remove the hit asteroid from the scene
            self.asteroids.remove(i)

        # If a medium asteroid is hit, it should break into 3 small asteroids
        if i.asize == 'Med':
            # two of which should fly off perpendicularly
            # to the direction of the laser beam
            piece_1 = Asteroid(self.SPACE)
            piece_1.asize = 'Small'
            piece_1.x = i.x
            piece_1.y = i.y
            piece_1.x_vel = - j.x_vel * speed_factor
            piece_1.y_vel = j.y_vel * speed_factor
            self.asteroids.append(piece_1)
            piece_2 = Asteroid(self.SPACE)
            piece_2.asize = 'Small'
            piece_2.x = i.x
            piece_2.y = i.y
            piece_2.x_vel = j.x_vel * speed_factor
            piece_2.y_vel = - j.y_vel * speed_factor
            self.asteroids.append(piece_2)
            # the third should fly off in the same direction that the laser
            # beam had been traveling.
            piece_3 = Asteroid(self.SPACE)
            piece_3.asize = 'Small'
            piece_3.x = i.x
            piece_3.y = i.y
            piece_3.x_vel = j.x_vel * speed_factor
            piece_3.y_vel = j.y_vel * speed_factor
            self.asteroids.append(piece_3)
            self.asteroids.remove(i)

        # If a small asteroid is hit, it disappears.
        if i.asize == 'Small':
            self.asteroids.remove(i)
