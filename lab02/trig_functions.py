import math

def main():
    angle = float(input("Enter an angle: "))
    radian = angle * (math.pi/180)
    cos_value = math.cos(radian)
    sin_value = math.sin(radian)
    print("The cosine of", angle, "is", cos_value)
    print("The sine of", angle, "is", sin_value)

main()