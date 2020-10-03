import turtle
import math


def main():
    """
    Draws a circle and a star using turtle
    """
    # set up magic numbers and calculate radius
    SIDE = 500
    ANGLE = 144
    SMALL_ANGLE = 18
    STRAIGHT_ANGLE = 90
    radius = SIDE / math.sqrt((5 + math.sqrt(5)) / 2)
    diameter = radius * 2

    # set up the coordinate that centers the shape
    start_x = 0
    start_y = -radius
    setup = SIDE * 2
    turtle.setup(setup, setup)

    # go to the initial point for drawing the circle
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    circle(ANGLE, radius)

    # go to the point for drawing the star
    turtle.setheading(STRAIGHT_ANGLE)
    turtle.penup()
    turtle.forward(diameter)
    turtle.right(ANGLE + SMALL_ANGLE)
    turtle.pendown()
    star(SIDE, ANGLE)

    turtle.done()


def circle(ANGLE, radius):
    # draw the circle and fill with color
    turtle.fillcolor("cyan")
    turtle.begin_fill()
    turtle.pencolor("blue")
    turtle.circle(radius)
    turtle.end_fill()


def star(SIDE, ANGLE):
    # draw the star and fill with color
    turtle.pencolor("red")
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for side in range(5):
        turtle.forward(SIDE)
        turtle.right(ANGLE)
    turtle.end_fill()


main()
