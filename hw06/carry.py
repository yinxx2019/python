def main():
    """
     prompts the user for two integers of any length and adds them together
     also counts the number of times the "carry" operation needs
    """
    # get two numbers from user input
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    # call sum function and carry function
    calc_sum(num1, num2)
    calc_carry(num1, num2)


def calc_sum(num1, num2):
    # calculate the sum of two numbers and print
    sum = int(num1) + int(num2)
    print(num1, "+", num2, "=", sum)


def calc_carry(num1, num2):
    # first set carry variable to loop to update value later
    carry = 0
    carry_next_column = 0
    # set condition to get the carry checking range
    if int(num1) <= int(num2):
        # add 0s to the shorter number to keep the digits consistent
        num1 = "0" * (len(num2) - len(num1)) + num1
        # reverse the string so that carry can be counted from the first digit
        shorter = num1[::-1]
        longer = num2[::-1]
    else:
        num2 = "0" * (len(num1) - len(num2)) + num2
        shorter = num2[::-1]
        longer = num1[::-1]
    carry_range = len(longer)
    # loop to check if there's any carry
    for x in range(carry_range):
        sum_digit = int(longer[x]) + int(shorter[x]) + carry_next_column
        carry_next_column = 0
        if sum_digit >= 10:
            carry += 1
            carry_next_column = 1

    print("Number of carries: ", carry)


main()
