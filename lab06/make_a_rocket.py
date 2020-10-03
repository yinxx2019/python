import sys
import math


def main(fuselage_length, width):
    """
    Draws a rocket with nose cone, fuselage and tail
    """

    # check if there's the stripped compand
    try:
        optional_argument = sys.argv[3]
    except Exception:
        optional_argument = None

    # call functions
    nose_cone(fuselage_length)
    fuselage(width, fuselage_length, optional_argument)
    tail(width, fuselage_length)


def nose_cone(fuselage_length):
    # draws the nose cone with conditions for odd and even length
    if fuselage_length % 2 != 0:
        nose_height = int((fuselage_length - 1) / 2)
        for rows in range(nose_height):
            space = int(nose_height - rows)
            asterisk = 2 * rows + 1
            print(" " * space + "*" * asterisk + " " * space)
    else:
        nose_height = int((fuselage_length / 2) - 1)
        for rows in range(nose_height):
            space = int((nose_height / 2) - rows + 2)
            asterisk = 2 * rows + 2
            print(" " * space + "*" * asterisk + " " * space)


def fuselage(width, fuselage_length, optional_argument):
    # draws the fuselage with conditions for length and stripped
    for rows in range(width):
        if optional_argument == "striped":
            if fuselage_length % 2 == 0:
                half_height = int(fuselage_length / 2)
                for rows in range(half_height):
                    print("_" * fuselage_length)
                for rows in range(half_height):
                    print("X" * fuselage_length)
            else:
                striped_height = int((fuselage_length - 1) / 2)
                X_height = int((fuselage_length + 1) / 2)
                for rows in range(striped_height):
                    print("_" * fuselage_length)
                for rows in range(X_height):
                    print("X" * fuselage_length)
        else:
            for rows in range(fuselage_length):
                print("X" * fuselage_length)


def tail(width, fuselage_length):
    # draws the tail with conditions for odd and even length
    tail_height = int(math.ceil(fuselage_length / 2) - width + 1)
    for rows in range(tail_height):
        if fuselage_length % 2 != 0:
            space = tail_height - 1 - rows
            asterisk = int(fuselage_length / 2 + rows * 2)
            print(" " * space + "*" * asterisk + " " * space)
        else:
            asterisk = 2 * (rows + 2)
            space = int((fuselage_length - asterisk) / 2)
            print(" " * space + "*" * asterisk + " " * space)
    print("*" * fuselage_length)


main(int(sys.argv[1]), int(sys.argv[2]))
