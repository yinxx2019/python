

def main():
    """
    Calculate triangular numbers by prompting the user for inputs
    """
    num = input("Enter a number, or enter 'done': ")
    triangular_number_function(num)


def triangular_number_function(num):
    triangular_number_list = []
    # use while loop to prompt for input
    while num != "done":
        triangular_number = int(((1 + int(num)) * int(num)) / 2)
        print("The triangular number for", num, "is", triangular_number)
        # update the list
        triangular_number_list.append(triangular_number)
        num = input("Enter another number, or enter 'done': ")
    else:
        print(triangular_number_list)


main()
