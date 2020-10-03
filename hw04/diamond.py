import math


def main():
    height = int(input("Type the height of your diamond "))

    # top half
    for rows in range(math.ceil(height / 2)):
        space = int(math.ceil(height / 2) - rows - 1)
        print(" " * space + "*" * (2 * rows + 1) + " " * space)

    # bottom half
    for rows in range(math.ceil(height / 2) + 1, height + 1):
        # set the condition for even height
        if height % 2 == 0:
            space = int(abs(math.ceil(height / 2 + 1) - rows))
            print(" " * space + "*" * (2 * (height - rows) + 1) + " " * space)
        # set the condition for odd height
        else:
            space = int(abs(math.ceil(height / 2) - rows))
            print(" " * space + "*" * (2 * (height - rows) + 1) + " " * space)


main()
