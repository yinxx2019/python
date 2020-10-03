# Xiaoxia Yin
# This program can generate username and password corresponding to user input

import random as rnd


# main function will generate username and password for users by a series of
# loop and string / numerical methods
def main():
    '''
    main function gets user's input about their first and last name and
    favorite words. Then it will generate username and password by selecting
    certain index in the user input

    None -> None
    '''
    # user input
    print("Welcome to the username and password generator!")
    first = input("Please enter your first name: ")
    last = input("Please enter your last name: ")
    word = input("Please enter your favorite word: ")

    # username section

    # empty string for filling characters later
    username_l = ""
    i = 0

    if len(last) >= 7:
        # loop for lastname longer than or equal to 7 characters
        while i < 7:
            username_l += last[i]
            i += 1
            username = first[0].lower() + username_l.lower() \
                + str(rnd.randint(0, 99))
    else:
        # loop for lastname shorter than 7 characters
        for i in range(len(last)):
            username_l += last[i]
            star = "*" * (7 - len(last))
            username = first[0].lower() + username_l.lower() \
                + star + str(rnd.randint(0, 99))
    print("Thank you " + first + ", your username is " + username)

    print("Here are three suggested passwords for you to consider: ")

    # password 1 section
    password_1 = (first + last).lower()

    # create list of characters and their replacements
    characters = ["a", "l", "s", "o", "x", "i", "y"]
    characters_change = ["@", "1", "$", "0", "*", "!", "9"]

    j = 0
    # loop to find all 7 characters and replace them
    while j < 7:
        password_1 = password_1.replace(characters[j], characters_change[j])
        j += 1
    print(password_1)

    # password 2 section that converts first and last characters for each
    password_2 = first[0].lower() + first[len(first) - 1].upper() \
        + last[0].lower() + last[len(last) - 1].upper() \
        + word[0].lower() + word[len(word) - 1].upper()
    print(password_2)

    # password 3 that selects a random portion for each
    password_3_f = first[0:rnd.randint(1, len(first))]
    password_3_l = last[0:rnd.randint(1, len(last))]
    password_3_w = word[0:rnd.randint(1, len(word))]

    password_3 = password_3_f + password_3_l + password_3_w
    print(password_3)


main()
