import sys


def main(n):
    # initiate the sequence
    sequence = [0, 1]

    # check if the user input a value no more than one
    if n <= 1:
        print("Try again with a number more than 1")
    else:
        # loop to fill the rest of the sequence
        for num in range(int(n - 2)):
            sequence.append(sequence[num] + sequence[num + 1])
        print(sequence)


main(int(sys.argv[1]))
