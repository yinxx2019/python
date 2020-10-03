import random as rnd


def main():
    # print an intro message
    print("Welcome to the Guessing Game!")

    # draw a random integer in a range of 1 to 50
    num = rnd.randint(1, 50)

    # use print when testing
    print(num)

    # ask user to input a number and store it in the variable
    user = int(input("I picked a number between 1 and 50. Try and guess! "))

    # measure times of guessing
    i = 1

    # loop to check differences between numbers
    while user != num:
        # store the differece between two numers in a variable
        difference = abs(user - num)
        i += 1
        if difference == 1:
            user = int(input("Scalding hot! Guess one more time! "))
        elif difference == 2:
            user = int(input("Extremely warm! Guess one more time! "))
        elif difference == 3:
            user = int(input("Very warm! Guess one more time! "))
        elif difference > 3 and difference <= 5:
            user = int(input("Warm. Guess one more time! "))
        elif difference > 5 and difference <= 8:
            user = int(input("Cold. Guess one more time! "))
        elif difference > 8 and difference <= 13:
            user = int(input("Very cold. Guess one more time! "))
        elif difference > 13 and difference <= 20:
            user = int(input("Extremely cold. Guess one more time! "))
        elif difference > 20:
            user = int(input("Icy freezing miserably cold. Guess again! "))
    else:
        print("Congratulations. You figured it out in", i, "tries.")

    # loop to check times of guessing
    if i == 1:
        print("That was lucky!")
    elif i >= 2 and i <= 4:
        print("That was amazing!")
    elif i >= 5 and i <= 6:
        print("That was okay.")
    elif i == 7:
        print("Meh.")
    elif i >= 8 and i <= 9:
        print("This is not your game.")
    elif i >= 10:
        print("You are the worst guesser I've ever seen.")


main()
