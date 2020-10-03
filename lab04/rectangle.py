

def main():

    symbol = input("Type a symbol you would like to use to make a rectangle ")
    width = int(input("Type a width "))
    height = int(input("Type a height "))

    # loop to test if the input number is too small
    while height < 2 or width < 2:
        print("The value is too small. ")
        if width < 2:
            width = int(input("Type a width value higher than 2. "))
        elif height < 2:
            height = int(input("Type a height value higher than 2. "))

    # print top line of the rectangle
    print(symbol * width)

    # print body lines of the rectangle fillied with spaces
    for edge in range(height - 2):
        print(symbol + " " * (width - 2) + symbol)

    # print bottom line of the rectangle
    print(symbol * width)


main()
