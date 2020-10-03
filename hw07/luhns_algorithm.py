def main():
    """
    validate a variety of identification numbers by
    the modulus 10 or mod 10 algorithm
    """
    # get account number from user input
    acc_num = input("Enter the account number: ")
    # loop to check if input contains digit only
    while all(x.isdigit() for x in acc_num) is False:
        acc_num = input("Enter the account number (digits only): ")
    calc(acc_num)


def calc(acc_num):
    # reverse the account number for calculation later
    rtl_acc_num = acc_num[::-1]
    # store doubled value later
    double = 0
    sum_digits = []
    TWO = 2
    TEN = 10
    ONE = 1
    # loop to double every other digit from right to left
    for x in range(len(rtl_acc_num)):
        # since index starts from 0, we should double all odd ones
        if x % TWO != 0:
            # double the digit
            double = str(int(rtl_acc_num[x]) * TWO)
            if len(double) > ONE:
                double = int(double[0]) + int(double[1])
        else:
            # keep the original digit
            double = rtl_acc_num[x]
        # append new digits to the sum list
        sum_digits.append(double)

    # sum all digits to validate if divisible by 10
    sum = 0
    for i in sum_digits:
        sum += int(i)
    if sum % TEN != 0:
        print("Not valid")
    else:
        print("Valid")


main()
