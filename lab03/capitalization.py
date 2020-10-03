def main():
    # ask user to input a word and convert it to lowercases
    user = input("Type a word: ").lower()

    # create a variable with a list of vowels
    vowels = ["a", "e", "i", "o", "u"]

    # create a variable with uppercase vowels for replacement later
    vowels_cap = ["A", "E", "I", "O", "U"]

    # count for the vowels varaiable list
    i = 0

    # loop to find all 5 items in the vowels list
    while i < 5:
        user = user.replace(vowels[i], vowels_cap[i])
        i += 1

    # print the user message with all vowels replaced to uppercase
    print(user)


main()
