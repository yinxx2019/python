import math

def main():
    x1 = float(input("Enter a value for first's number's X-axis value: "))
    y1 = float(input("Enter a value for first's number's Y-axis value: "))
    x2 = float(input("Enter a value for first's number's X-axis value: "))
    y2 = float(input("Enter a value for first's number's Y-axis value: "))

    distance1 = float(x1-y1)
    distance2 = float(x2-y2)

    #calculate distance using exponentiation
    distancexy = (distance1** 2+ distance2** 2) ** 0.5
    #calculate distance using math
    distanceyx = math.sqrt(math.pow(distance1, 2) + math.pow(distance2, 2))

    print("The distance between two points is",distancexy)
    print("The distance between two points is",distanceyx)

main()