import sys
import math


def main():

    # define center in the coordinate system
    x = 0
    y = 0

    # define radius from command line
    radius = int(sys.argv[1])

    # loop y axis for multi-line
    for y in range(radius, -radius, -1):

        # define string to fill with spaces and "o"s
        character = ""

        # loop x axis for each line
        for x in range(-radius, radius):
            distance = math.sqrt(math.pow(y, 2) + math.pow(x, 2))
            if distance < radius:
                character = character + "o"
            else:
                character = character + " "
        print(character)


main()
