

def main():

    # create an empty list for filling user input numbers
    num_list = []

    # count times of input
    i = 0
    print(("Enter a magic number "))

    # loop three times for three numbers
    while i <= 2:
        num_list.append(input())
        i += 1

    # the comment below is for testing purpose
    # print(num_list)

    # calculate sum for 8 directions
    sum1 = int(num_list[0][0]) + int(num_list[0][1]) + int(num_list[0][2])
    sum2 = int(num_list[1][0]) + int(num_list[1][1]) + int(num_list[1][2])
    sum3 = int(num_list[2][0]) + int(num_list[2][1]) + int(num_list[2][2])
    sum4 = int(num_list[0][0]) + int(num_list[1][0]) + int(num_list[2][0])
    sum5 = int(num_list[0][1]) + int(num_list[1][1]) + int(num_list[2][1])
    sum6 = int(num_list[0][2]) + int(num_list[1][2]) + int(num_list[2][2])
    sum7 = int(num_list[0][0]) + int(num_list[1][1]) + int(num_list[2][2])
    sum8 = int(num_list[0][2]) + int(num_list[1][1]) + int(num_list[2][0])

    # the comment below is for testing purpose
    # print(sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8)

    # test if the sum of all directions equals to 15
    if sum1 == sum2 == sum3 == sum4 == sum5 == sum6 == sum7 == sum8 == 15:
        print("This is a magic square!")
    else:
        print("Not a magic square!")


main()
