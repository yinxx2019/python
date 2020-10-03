import re


def main():
    # get file name from user input
    filename = input("Enter the file name: ")
    try:
        # read file
        f = open(filename, "r")  # encoding="utf8"
    # create print message for exception
    except Exception:
        print("Can't open", filename, ". Try something else! ")
        return

    txt = f.read()

    # word count
    words = txt.split()
    word_count = len(words)
    print("Words:", word_count)

    # character count
    character = 0
    for i in txt:
        if i == " " or i == "\n":
            character = character
        else:
            character += 1
    print("Characters: ", character)

    # letter and number count
    letter_and_number = 0
    for i in txt:
        if i in re.findall("\\w", txt):
            letter_and_number += 1
        else:
            letter_and_number = letter_and_number
    print("Letters & numbers:", letter_and_number)

    # the other way I tried earilier is to use character minus punctuation
    # counts. This way the program runs quicker but I need to look up all
    # punctutations manually.
    puntucation = 0
    puntucation_list = ["-", ",", ".", "\"", "\'", "(", ")"]

    for i in txt:
        if i in puntucation_list:
            puntucation += 1
        else:
            puntucation = puntucation
    letter_number = character - puntucation
    print("Letters & numbers:", letter_number)


main()
