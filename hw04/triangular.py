import sys


def main(n):
    # calculate triangular number using formula
    sum = int(((1 + n) * n) / 2)
    print(sum)


main(int(sys.argv[1]))
