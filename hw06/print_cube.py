def main():
    """
    draws 2D cubes with sizes from user input
    """
    n = int(input("Input cube size (multiple of 2): "))
    while n % 2 != 0 or n < 2:
        n = int(input("Invalid value. Input cube size (multiple of 2): "))
    else:
        cube(n)


def cube(n):
    double_n = n * 2
    # draw top side
    diag_edge = int(n / 2)
    space_top_line = diag_edge + 1

    # first line of the top side
    print(" " * space_top_line + "+" + "-" * double_n + "+")
    # middle lines of the top side
    for row in range(diag_edge):
        space = space_top_line - (row + 1)
        print(" " * space + "/" + " " * double_n + "/" + " " * row + "|")
    # last line of the top side, also the first line of the front side
    print("+" + "-" * double_n + "+" + " " * diag_edge + "|")

    # draw front side
    for row in range(n - space_top_line):
        print("|" + " " * double_n + "|" + " " * diag_edge + "|")
    # draw diagnal corner
    print("|" + " " * double_n + "|" + " " * diag_edge + "+")
    for row in range(space_top_line - 1):
        print("|" + " " * double_n + "|" + " " * (diag_edge - row - 1) + "/")
    # last line of the front side
    print("+" + "-" * double_n + "+")


main()
