import random as rnd


def main():
    # print default message
    print("Welcome to the DMV (estimated wait time is 3 hours)")

    # ask users to input name and date of birth
    name = input("Please enter your first, middle, and last name: ")
    date_of_birth = input("Enter date of birth (MM/DD/YY):")

    # Randomly draw a 7 digits number
    # Zack and Drew told me it's fine to ignore the situation
    # of starting with 0 for this assignment
    license_number = rnd.randint(1000000, 9999999)

    # using split to divide and find first, middle and last names
    split_name = name.split()
    last_name = split_name[2].capitalize()
    first_name = split_name[0].capitalize()
    middle_name = split_name[1].capitalize()

    # using rfind to locate the slash before the year
    expiration_index = date_of_birth.rfind("/")
    expiration_date = date_of_birth[:expiration_index + 1]

    # print all messages
    print("Washington Driver License")
    print("DL", license_number)
    print("LN", last_name)
    print("FN", first_name, middle_name)
    print("DOB", date_of_birth)
    print("EXP", expiration_date + "21")


main()
