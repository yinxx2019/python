

def main():

    width = int(input("Type an odd number "))
    while width % 2 == 0:
        width = int(input("Type an odd number "))

    else:
        # calculate the height for the triangle
        column = int((width - 1) / 2)

        # print first line and center the "*"
        print(" " * column + "*" + " " * column)

        # loop to print two sides
        for row in range(column - 1):
            print(" " * (column - row - 1) + "/" + " " * (2 * row + 1)
                  + "\\")

        # print the bottom side
        print("/" + "_" * (width - 2) + "\\")


main()
